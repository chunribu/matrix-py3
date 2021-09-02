import os, sys
from pebble import concurrent
from functools import wraps
from .matrix import matrix

ALIVE = 1
@concurrent.thread
def loop():
    matrix(0)
    return

def cool_matrix(fn):
    @concurrent.thread
    def async_fn(*args, **kwargs):
        return fn(*args, **kwargs)
    @wraps
    def wrapper(*args, **kwargs):
        my_loop = loop()
        future = async_fn(*args, **kwargs)
        try:
            result = future.result()
        except Exception as e:
            result=False
            print(e)
        my_loop.cancel()
        return result
    return wrapper

@concurrent.thread
def run_cmd(cmd):
    return os.system(cmd)

def cool_matrix_cmd():
    my_loop = loop()
    args = sys.argv
    args.pop(0)
    cmd = " ".join(args) + " >> cool.log"
    future = run_cmd(cmd)
    try:
        result = future.result()
    except Exception as e:
        result=False
        print(e)
    my_loop.cancel()
    return result