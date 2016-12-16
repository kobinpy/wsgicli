=======
WSGICLI
=======

.. image:: https://travis-ci.org/kobinpy/wsgicli.svg?branch=master
    :target: https://travis-ci.org/kobinpy/wsgicli

.. image:: https://badge.fury.io/py/wsgicli.svg
    :target: https://badge.fury.io/py/wsgicli

Command Line Interface for developing WSGI application.
This library has following features.

**Run WSGI Application in wsgiref**

* Run wsgi application with specified host and port.
* Serving Static files.
* Live reloading.
* line by line profiling.
* Validating your WSGI application complying with PEP3333 compliance.

**Run python interpreter**

* Supported interpreters are python(plain), ipython, bpython, ptpython and ptipython.
* Automatically import SQLAlchemy and peewee models when run the interpreter.


Commands
========

Run command
-----------

Synopsis
~~~~~~~~

.. code-block:: console

   $ wsgicli run [FILEPATH] [WSGIAPP] [Options]

==  =========  ====================  ========================================================
No  Arguments  Environment Variable  Description
==  =========  ====================  ========================================================
 1  FILEPATH   ``WSGICLI_FILE``      The file path for your WSGI application.
 2  WSGIAPP    ``WSGICLI_WSGI_APP``  The variable name of your wsgi application object.
==  =========  ====================  ========================================================

==================================  =========================  =================  ====================================================================
Options                             Environment Variable       Default            Description
==================================  =========================  =================  ====================================================================
``-h`` ``--host``                   ``WSGICLI_HOST``           ``127.0.0.1``      The hostname to bind to.
``-p`` ``--port``                   ``WSGICLI_PORT``           8000               The port to bind to.
``--reload`` / ``--no-reload``      ``WSGICLI_RELOAD``         False              Enable live reloading.
``--interval``                      ``WSGICLI_INTERVAL``       1                  Interval time to check file changed for reloading (sec).
``--static`` / ``--no-static``      ``WSGICLI_STATIC``         False              Enable static file serving.
``--static-root``                   ``WSGICLI_STATIC_ROOT``    ``/static/``       URL path to static files.
``--static-dirs``                   ``WSGICLI_STATIC_DIRS``    ``['./static/']``  Directories to static files (multiple).
``--lineprof`` / ``--no-lineprof``  ``WSGICLI_LINEPROF``       False              Enable line profiler.
``--lineprof-file``                 ``WSGICLI_LINEPROF_FILE``  WSGIAPP(2nd arg)   The filename profiled by line-profiler.
``--validate`` / ``--no-validate``  ``WSGICLI_VALIDATE``       False              Validating your WSGI application complying with PEP3333.
``--help``                                                                        Show help text.
==================================  =========================  =================  ====================================================================

Example
~~~~~~~

.. code-block:: console

   $ wsgicli run main.py app -p 8080 --reload

.. image:: https://raw.githubusercontent.com/kobinpy/wsgicli/master/resources/wsgicli-live-reloading-demo.gif
   :alt: WSGICLI Run Command DEMO
   :align: center


Shell command
-------------

Synopsis
~~~~~~~~

.. code-block:: console

   $ wsgicli shell [FILEPATH] [WSGIAPP] [Options]

==  =========  =====================  ========================================================
No  Arguments  Environment Variable   Description
==  =========  =====================  ========================================================
 1  FILEPATH   ``WSGICLI_FILE_PATH``  The file path for your WSGI application.
 2  WSGIAPP    ``WSGICLI_WSGI_APP``   The variable name of your wsgi application object.
==  =========  =====================  ========================================================

==================================  ========================  ==============  ====================================================================
Options                             Environment Variable      Default         Description
==================================  ========================  ==============  ====================================================================
``-i`` ``--interpreter``            ``WSGICLI_INTERPRETER``   ``'python'``    Supported interpreters are ipython, bpython, ptpython and ptipython.
``--models`` / ``--no-models``      ``WSGICLI_MODELS``        True            Automatically import ORM table definition from your app.
``--help``                                                                    Show help text.
==================================  ========================  ==============  ====================================================================


Example
~~~~~~~

.. code-block:: console

   $ wsgicli shell main.py app --interpreter ipython

.. image:: https://raw.githubusercontent.com/kobinpy/wsgicli/master/resources/wsgicli-shell-demo.gif
   :alt: WSGICLI Run Command DEMO
   :align: center


Requirements
============

- Python 3.3 or later
- click
- wsgi-static-middleware
- wsgi-lineprof


License
=======

This software is licensed under the MIT License.
