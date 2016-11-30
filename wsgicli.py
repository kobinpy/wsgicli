import click
from importlib.machinery import SourceFileLoader
import os
import sys
import time
import threading
import _thread
from wsgiref.simple_server import make_server


#####################################################################################
# For run server
#####################################################################################
def run_server(app, host, port):
    print('Start: {host}:{port}'.format(host=host, port=port))
    httpd = make_server(host, port, app)
    httpd.serve_forever()


#####################################################################################
# For reloading server when detected python files changes.
#####################################################################################
EXIT_STATUS_RELOAD = 3


class FileCheckerThread(threading.Thread):
    # This class is copied and pasted from following source code of Bottle.
    #   https://github.com/bottlepy/bottle/blob/master/bottle.py#L3647-L3686
    """ Interrupt main-thread as soon as a changed module file is detected,
        the lockfile gets deleted or gets too old. """

    def __init__(self, lockfile, interval):
        threading.Thread.__init__(self)
        self.daemon = True
        self.lockfile, self.interval = lockfile, interval
        #: Is one of 'reload', 'error' or 'exit'
        self.status = None

    def run(self):
        files = dict()

        for module in list(sys.modules.values()):
            path = getattr(module, '__file__', '')
            if path[-4:] in ('.pyo', '.pyc'):
                path = path[:-1]
            if path and os.path.exists(path):
                files[path] = os.stat(path).st_mtime

        while not self.status:
            if not os.path.exists(self.lockfile) or \
                    os.stat(self.lockfile).st_mtime < time.time() - self.interval - 5:
                self.status = 'error'
                _thread.interrupt_main()
            for path, last_mtime in files.items():
                if not os.path.exists(path) or os.stat(path).st_mtime > last_mtime:
                    self.status = 'reload'
                    _thread.interrupt_main()
                    break
            time.sleep(self.interval)

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, *_):
        if not self.status:
            self.status = 'exit'  # silent exit
        self.join()
        return exc_type is not None and issubclass(exc_type, KeyboardInterrupt)


def run_live_reloading_server(interval, app, host, port):
    if not os.environ.get('WSGICLI_CHILD'):
        import subprocess
        import tempfile
        lockfile = None
        try:
            fd, lockfile = tempfile.mkstemp(prefix='wsgicli.', suffix='.lock')
            os.close(fd)  # We only need this file to exist. We never write to it
            while os.path.exists(lockfile):
                args = [sys.executable] + sys.argv
                environ = os.environ.copy()
                environ['WSGICLI_CHILD'] = 'true'
                environ['WSGICLI_LOCKFILE'] = lockfile
                p = subprocess.Popen(args, env=environ)
                while p.poll() is None:  # Busy wait...
                    os.utime(lockfile, None)  # Alive! If lockfile is unlinked, it raises FileNotFoundError.
                    time.sleep(interval)
                if p.poll() != EXIT_STATUS_RELOAD:
                    if os.path.exists(lockfile):
                        os.unlink(lockfile)
                        sys.exit(p.poll())
        except KeyboardInterrupt:
            pass
        finally:
            if os.path.exists(lockfile):
                os.unlink(lockfile)
        return

    try:
        lockfile = os.environ.get('WSGICLI_LOCKFILE')
        bgcheck = FileCheckerThread(lockfile, interval)
        with bgcheck:
            run_server(app=app, host=host, port=port)
        if bgcheck.status == 'reload':
            sys.exit(EXIT_STATUS_RELOAD)
    except KeyboardInterrupt:
        pass
    except (SystemExit, MemoryError):
        raise
    except:
        time.sleep(interval)
        sys.exit(3)


#####################################################################################
# Command Line Interface
#####################################################################################
@click.command()
@click.argument('filepath', nargs=1)
@click.argument('wsgiapp', nargs=1)
@click.option('--host', '-h', type=click.STRING, default='127.0.0.1',
              help='The interface to bind to.')
@click.option('--port', '-p', type=click.INT, default=8000, help='The port to bind to.')
@click.option('--reload/--no-reload', default=None, help='Enable live reloading')
@click.option('--interval', type=click.INT, default=1,
              help='Interval time to check file changed for reloading')
@click.option('--static/--no-static', default=None, help='Enable static file serving')
@click.option('--static-root', default='static', help='URL path to static files')
@click.option('--static-dirs', default=['./static/'], multiple=True,
              help='Directories for static files')
@click.option('--lineprof/--no-lineprof', help='Enable line profiler')
@click.option('--lineprof-file', multiple=True, help='The filename profiled by line-profiler')
def cmd(filepath, wsgiapp, host, port, reload, interval,
        static, static_root, static_dirs, lineprof, lineprof_file):
    """
    Runs a development server for WSGI Application.

    Usage:

        $ wsgicli hello.py app -h 0.0.0.0 -p 5000

        $ wsgicli hello.py app --reload

        $ wsgicli hello.py app --static --static-root /static/ --static-dirs ./static/

        $ wsgicli hello.py app --lineprof
    """
    module = SourceFileLoader('module', filepath).load_module()
    app = getattr(module, wsgiapp)

    if static:
        from wsgi_static_middleware import StaticMiddleware
        app = StaticMiddleware(app, static_root=static_root, static_dirs=static_dirs)

    if lineprof:
        # Caution: wsgi-lineprof is still pre-alpha. Except breaking API Changes.
        from wsgi_lineprof.middleware import LineProfilerMiddleware
        from wsgi_lineprof.filters import FilenameFilter, TotalTimeSorter

        if lineprof_file:
            # Now wsgi-lineprof is now supported only 1 file checking.
            lineprof_file = lineprof_file[0]
        else:
            lineprof_file = filepath.split('/')[-1] if '/' in filepath else filepath
        filters = [FilenameFilter(lineprof_file), TotalTimeSorter()]
        app = LineProfilerMiddleware(app, filters=filters)

    if reload:
        run_live_reloading_server(interval, app=app, host=host, port=port)
    else:
        run_server(app=app, host=host, port=port)


if __name__ == '__main__':
    cmd()
