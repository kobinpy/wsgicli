import time


def do_nothing():
    time.sleep(0.5)


def app(env, start_response):
    do_nothing()
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    return [b'Hello World']
