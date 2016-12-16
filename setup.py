import os
from setuptools import setup

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_PATH, 'README.rst')).read()

__version__ = '0.4.0'
__author__ = 'Masashi Shibata <contact@c-bata.link>'
__author_email__ = 'contact@c-bata.link'
__license__ = 'MIT License'
__classifiers__ = (
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
    'Environment :: Web Environment',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
)


setup(
    name='wsgicli',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url='https://github.com/kobinpy/wsgicli',
    description='Command Line Interface for developing WSGI application.',
    long_description=README,
    classifiers=__classifiers__,
    py_modules=['wsgicli'],
    install_requires=['click', 'wsgi-static-middleware', 'wsgi_lineprof'],
    keywords='web framework wsgi',
    license=__license__,
    include_package_data=True,
    test_suite='tests',
    entry_points={'console_scripts': ['wsgicli = wsgicli:cli']},
)
