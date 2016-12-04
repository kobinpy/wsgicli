# Example

## wsgicli run

### Basic Example

```console
$ wsgicli run hello.py app --reload
Start: 127.0.0.1:8000
127.0.0.1 - - [04/Dec/2016 12:24:16] "GET / HTTP/1.1" 200 11
```

### Profiling Example


```console
$ wsgicli run profiled_example.py app --lineprof
Start: 127.0.0.1:8000
Time unit: 1e-06 [sec]

File: profiled_example.py
Name: app
Total time: 0.500785 [sec]
  Line      Hits         Time  Code
===================================
     8                         def app(env, start_response):
     9         1       500112      do_nothing()
    10         1          672      start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    11         1            1      return [b'Hello World']

File: profiled_example.py
Name: do_nothing
Total time: 0.500087 [sec]
  Line      Hits         Time  Code
===================================
     4                         def do_nothing():
     5         1       500087      time.sleep(0.5)

127.0.0.1 - - [04/Dec/2016 12:25:07] "GET / HTTP/1.1" 200 11
```


## wsgicli shell

Supported interpreters are:

- python (plain)
- ipython
- bpython
- ptpython
- ptipython

### Automatically import Database Definition

```console
$ wsgicli shell model_import_test.py
Base is imported!
Task is imported!
BaseModel is imported!
Model is imported!
Tweet is imported!
User is imported!
db is imported!
Python 3.5.2 (default, Oct  1 2016, 04:21:35) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Tweet
<class 'peewee_models.Tweet'>
>>> User
<class 'peewee_models.User'>
>>> Task
<class 'sqlalchemy_models.Task'>
```

