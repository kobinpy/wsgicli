=======
WSGICLI
=======

Command Line Interface for developing WSGI application.
This library has following features.

* Run wsgi application with specified host and port.
* Serving Static files.
* Based click


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

   $ wsgicli main:app

Run this application in specified host(default: localhost) and port(default: 8000):

.. code-block:: console

   $ wsgicli main:app -h 0.0.0.0 -p 8080


Static files
------------

Run wsgi application and serve static files:

Create `static/style.css`:

.. code-block:: css

   .container {
      max-width: 980px;
   }

And run:

.. code-block:: console

   $ wsgicli main:app -p 8000 --staticroot static --staticdir static/
   $ curl http://localhost:8000/static/main.css
   .container {
      max-width: 980px;
   }


Requirements
============

- Python 2.7 and Python 3.3 or later
- click

License
=======

This software is licensed under the MIT License.
