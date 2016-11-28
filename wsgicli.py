import click
from wsgi_static_middleware import StaticMiddleware
from wsgiref.simple_server import make_server
import importlib


@click.command('run', short_help='Runs a development server.')
@click.argument('wsgi')
@click.option('--host', '-h', default='127.0.0.1', help='The interface to bind to.')
@click.option('--port', '-p', default=8000, help='The port to bind to.')
@click.option('--enable-static/--disable-static', default=None, help='Static file serving')
@click.option('--static-root', default='static', help='Static root')
@click.option('--static-dir', default='./static/', multiple=True,
              help='Directories for static files')
def cmd(wsgi, host, port, enable_static, static_root, static_dir, verbose):
    """Runs a development server for WSGI Application"""
    file, obj = wsgi.split(':')
    app = getattr(importlib.import_module(file), obj)
    if enable_static:
        app = StaticMiddleware(app, static_root=static_root, static_dirs=static_dir)
    httpd = make_server(host, port, app)
    httpd.serve_forever()

if __name__ == '__main__':
    cmd()
