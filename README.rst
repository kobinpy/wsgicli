=======
WSGICLI
=======

Command Line Interface for developing WSGI application.
This library has following features.

* [x] Run wsgi application with specified host and port.
* [x] Serving Static files.
* [x] Live reloading.
* [ ] Several WSGI Server Support with abstract base classes.
* [ ] vmprof profiler.

How to use
==========

Basic Usage
-----------

Create ``main.py`` :

.. code-block:: python

   def app(env, start_response):
       start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
       return [b'Hello World']

Run this application using wsgiref:

.. code-block:: console

   $ wsgicli main.py app

Run this application in specified host(default: localhost) and port(default: 8000):

.. code-block:: console

   $ wsgicli main.py app -h 0.0.0.0 -p 8080


Static files
------------

Run wsgi application and serve static files:

Create ``static/style.css``:

.. code-block:: css

   .container {
      max-width: 980px;
   }

And run:

.. code-block:: console

   $ wsgicli main.py app -p 8000 --static --staticroot static --staticdirs static/
   $ curl http://localhost:8000/static/main.css
   .container {
      max-width: 980px;
   }


vmprof profiler
---------------

**Still Not Implemented**

Using vmprof and vmprof-server.

.. code-block:: console

   $ wsgicli main.py app -p 8000 --enable-profile --profile-port 8080

refs:

* https://github.com/vmprof/vmprof-python
* https://github.com/vmprof/vmprof-server

Arguments and Options
=====================

Arguments
---------

1. ``file`` : File path for your wsgi application.
2. ``obj`` : The variable name of your wsgi application object.

Options
-------

- ``-h`` ``--host`` : The interface to bind to. (default: ``127.0.0.1``).
- ``-p`` ``--port`` : The port to bind to. (default: ``8000``).
- ``--reload`` / ``--no-reload`` : Enable live reloading (default: ``--no-reload``).
- ``--interval`` : Interval time to check file changed for reloading (default: ``1``).
- ``--static`` / ``--no-static`` : Enable static file serving (default: ``--no-static``).
- ``--staticroot`` : URL path to static files (default: ``/static/``).
- ``--staticdirs`` : Directories to static files (default: ``./static``, multiple=true).
- ``--profile`` / ``--no-profile`` : Enable vmprof profiling (default: ``--no-profile``).
- ``--profile-port`` : Port number for vmprof server (default: ``8080``).

Environment Variables
---------------------

**Still Not Implemented**

- ``WSGICLI_TARGET``
- ``WSGICLI_PORT``
- ``WSGICLI_HOST``
- ``WSGICLI_RELOAD``
- ``WSGICLI_RELOAD_INTERVAL``
- ``WSGICLI_STATIC``
- ``WSGICLI_STATIC_ROOT``
- ``WSGICLI_STATIC_DIRS``
- ``WSGICLI_PROFILE``
- ``WSGICLI_PROFILE_PORT``

Why WSGICLI?
============

While developing WSGI Application and WSGI Middleware, I encountered some troublesome scenes.
I will explain it using actual code.

.. code-block:: python

   class SomeMiddleware:
       def __init__(self, app):
           self.app = app

       def __call__(self, env, start_response):
           return self.app(env, start_response)

This is a very simple WSGI middleware.
It is also fully compatible with the WSGI interface.
Let's use this Middleware with various WSGI frameworks.


In the case of Bottle
---------------------

.. code-block:: python

   from bottle import Bottle
   app = Bottle()

   @app.route('/hello/<name>')
   def index(name):
       return 'Hello World!'

   app = SomeMiddleware(app)

   if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8000)


As you can see, this program does not work.
``SomeMiddleware`` is compatible with the WSGI Interface, but ``run`` method does not exist.

However, ``app`` object satisfies the specification of WSGI, it can be executed using WSGI Server (gunicorn, etc.) as follows.

.. code-block:: console

   $ gunicorn -w main:app  -b 127.0.0.1:8000

So, how does Bottle use WSGI middleware?

.. code-block:: python

   import bottle
   app = SomeMiddleware(bottle.app())

   @bottle.route('/')
   def index():
     return 'Hello World!'

   if __name__ == '__main__':
       bottle.run(app=app, host='127.0.0.1', port=8000)


In Bottle, you can use WSGI Middleware by describing like this.
But although Bottle is a Micro Framework, it spends a little bit of code to accomplish this.

- https://github.com/bottlepy/bottle/blob/master/bottle.py#L3100-L3125
- https://github.com/bottlepy/bottle/blob/master/bottle.py#L3541-L3644

In the case of Flask
--------------------

Flask had similar problems until then.
But Flask now provides a Command Line Interface based on Click from v0.11 (See `Flask documentation <http://flask.pocoo.org/docs/0.11/quickstart/#a-minimal-application>`_ ).
This is a good idea.

Thinking about the role of WSGI Framework
-----------------------------------------

The ``run()`` method is useful for running WSGI Applications in development.
But is this really a function that the WSGI Framework should provide?

In the Kobin WSGI Framework that I am developing, I decided not to provide functions like `run()`.
Instead, Please use this library.

This library is designed to be widely used in the development of WSGI applications.
Please make use of your own WSGI Framework or projects that do not use WSGI Framework.

Requirements
============

- Python 3.3 or later
- click
- wsgi-static-middleware

License
=======

This software is licensed under the MIT License.
