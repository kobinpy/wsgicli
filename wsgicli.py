import click
from wsgi_static_middleware import StaticMiddleware
from wsgiref.simple_server import make_server
import importlib


@click.command('run', short_help='Runs a development server.')
@click.argument('wsgi')
@click.option('--host', '-h', default='127.0.0.1', help='The interface to bind to.')
@click.option('--port', '-p', default=8000, help='The port to bind to.')
@click.option('--reload/--no-reload', default=None, help='Enable or disable the reloader.')
def run_command(wsgi, host, port, reload):
    """Runs a development server for WSGI Application"""
    file, obj = wsgi.split(':')
    app = getattr(importlib.import_module(file), obj)
    httpd = make_server(host, port, app)
    httpd.serve_forever()
