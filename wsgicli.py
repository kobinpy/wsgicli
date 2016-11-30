import click
from wsgi_static_middleware import StaticMiddleware
from wsgiref.simple_server import make_server
from importlib.machinery import SourceFileLoader


@click.command()
@click.argument('filepath', nargs=1)
@click.argument('wsgiapp', nargs=1)
@click.option('--host', '-h', default='127.0.0.1', help='The interface to bind to.')
@click.option('--port', '-p', default=8000, help='The port to bind to.')
@click.option('--enable-static/--disable-static', default=None, help='Static file serving')
@click.option('--static-root', default='static', help='Static root')
@click.option('--static-dirs', default=['./static/'], multiple=True,
              help='Directories for static files')
def cmd(filepath, wsgiapp, host, port, enable_static, static_root, static_dirs):
    """Runs a development server for WSGI Application"""
    module = SourceFileLoader('module', filepath).load_module()
    app = getattr(module, wsgiapp)
    if enable_static:
        app = StaticMiddleware(app, static_root=static_root, static_dirs=static_dirs)
    httpd = make_server(host, port, app)
    httpd.serve_forever()

if __name__ == '__main__':
    cmd()
