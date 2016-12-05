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

Example
~~~~~~~

.. code-block:: console

   $ wsgicli run main.py app -p 8080 --reload

.. image:: https://raw.githubusercontent.com/kobinpy/wsgicli/master/resources/wsgicli-live-reloading-demo.gif
   :alt: WSGICLI Run Command DEMO
   :align: center

Arguments and Options
~~~~~~~~~~~~~~~~~~~~~

==  =========  ====================  ========================================================
    Argument   Environment Variable  Description
==  =========  ====================  ========================================================
 1  FILE       WSGICLI_FILE          The file path for your WSGI application.
 2  WSGIAPP    WSGICLI_WSGI_APP      The variable name of your wsgi application object.
==  =========  ====================  ========================================================

==================================  =================  =====================  ====================================================================
Options                             Default            Environment Variable   Description
==================================  =================  =====================  ====================================================================
``-h`` ``--host``                   ``127.0.0.1``      WSGICLI_HOST           The hostname to bind to.
``-p`` ``--port``                   8000               WSGICLI_PORT           The port to bind to.
``--reload`` / ``--no-reload``      False              WSGICLI_RELOAD         Enable live reloading.
``--interval``                      1                  WSGICLI_INTERVAL       Interval time to check file changed for reloading (sec).
``--static`` / ``--no-static``      False              WSGICLI_STATIC         Enable static file serving.
``--static-root``                   ``/static/``       WSGICLI_STATIC_ROOT    URL path to static files.
``--static-dirs``                   ``['./static/']``  WSGICLI_STATIC_DIRS    Directories to static files (multiple).
``--lineprof`` / ``--no-lineprof``  False              WSGICLI_LINEPROF       Enable line profiler.
``--lineprof-file``                 WSGIAPP(2nd arg)   WSGICLI_LINEPROF_FILE  The filename profiled by line-profiler.
``--validate`` / ``--no-validate``  False              WSGICLI_VALIDATE       Validating your WSGI application complying with PEP3333.
==================================  =================  =====================  ====================================================================


Shell command
-------------

Example
~~~~~~~

.. code-block:: console

   $ wsgicli shell main.py --interpreter ipython

.. image:: https://raw.githubusercontent.com/kobinpy/wsgicli/master/resources/wsgicli-shell-demo.gif
   :alt: WSGICLI Run Command DEMO
   :align: center

Arguments and Options
~~~~~~~~~~~~~~~~~~~~~

==  ===========  ====================  ========================================================
    Arguments    Environment Variable  Description
==  ===========  ====================  ========================================================
 1  FILE         WSGICLI_FILE          The file path for your WSGI application.
==  ===========  ====================  ========================================================

==================================  =================  =====================  ====================================================================
Options                             Default            Environment Variable   Description
==================================  =================  =====================  ====================================================================
``-i`` ``--interpreter``            ``'python'``       WSGICLI_INTERPRETER    Supported interpreters are ipython, bpython, ptpython and ptipython.
``--models`` / ``--no-models``      True               WSGICLI_MODELS         Automatically import ORM table definition from your app.
==================================  =================  =====================  ====================================================================


Requirements
============

- Python 3.3 or later
- click
- wsgi-static-middleware
- wsgi-lineprof


License
=======

This software is licensed under the MIT License.
