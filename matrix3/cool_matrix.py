import os, sys
from pebble import ProcessPool
from .matrix import matrix

def cool_matrix(fn, *args, **kw):
    with ProcessPool(max_workers=2) as pool:
        my_loop = pool.schedule(matrix)
        future = pool.schedule(fn, args=args, kwargs=kw)
        result = future.result()
        my_loop.cancel()
        return result

def run(cmd):
    os.system(cmd)

def cool_matrix_cmd():
    args = sys.argv
    args.pop(0)
    cmd = " ".join(args) + ">> cool.log"
    cool_matrix(run, cmd)
