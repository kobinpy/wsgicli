import click
from wsgi_static_middleware import StaticMiddleware
from wsgiref.simple_server import make_server

try:
    from importlib.machinery import SourceFileLoader
except ImportError:
    SourceFileLoader = None


def load_module_from_pyfile(path):
    if SourceFileLoader:
        wsgi_module = SourceFileLoader('wsgi_module', path).load_module()
    else:
        import types
        wsgi_module = types.ModuleType('wsgi_module')
        with open(path) as wsgi_file:
            exec(compile(wsgi_file.read(), path, 'exec'), wsgi_module.__dict__)
    return wsgi_module
