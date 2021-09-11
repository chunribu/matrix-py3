import os, sys, collections, time, random
from string import printable
from pebble import concurrent
from multiprocessing import Value
from functools import wraps

try:
    import curses
except ImportError:
    print("\nDependency 'curses' not found. \nTry: conda install ncurses\n")
    exit(0)

ALIVE = Value('i',1)
def loop(stdscr):
    CLEAR = False
    FG = curses.COLOR_GREEN
    BG = curses.COLOR_BLACK
    LETTERS_PER_UPDATE = 6
    PROBABILITY = 6
    UPDATES_PER_SECOND = 6
    rand_string = lambda c, l: "".join(random.choice(c) for _ in range(l))
    curses.curs_set(0)
    curses.init_pair(9, FG, BG)
    stdscr.bkgd(curses.color_pair(9))
    curses.start_color()
    size = stdscr.getmaxyx()
    MatrixPY = collections.namedtuple("MatrixPY", ["foreground", "background", "dispense"])
    matr = MatrixPY([], rand_string(printable.strip(), size[0] * size[1]), [])
    delta = 0
    lt = time.time()
    while ALIVE.value:
        if CLEAR:
            stdscr.clear()
        else:
            stdscr.erase()
        now = time.time()
        delta += (now - lt) * UPDATES_PER_SECOND
        lt = now
        while delta >= 1:
            if stdscr.getmaxyx() != size:
                return
            for _ in range(LETTERS_PER_UPDATE):
                matr.dispense.append(random.randint(0, size[1] - 1))
            for i, c in enumerate(matr.dispense):
                matr.foreground.append([0, c])
                if not random.randint(0, PROBABILITY):
                    del matr.dispense[i]
            for a, b in enumerate(matr.foreground):
                if b[0] < size[0] - 1:
                    stdscr.addstr(b[0], b[1],
                                    matr.background[b[0] * size[0] + b[1]],
                                    curses.color_pair(9))
                    b[0] += 1
                else:
                    del matr.foreground[a]
            delta -= 1
            stdscr.refresh()

def run_loop():
    curses.wrapper(loop)

# def cool_matrix(fn):
#     @concurrent.thread
#     def async_fn(*args, **kwargs):
#         return fn(*args, **kwargs)
#     @wraps
#     def wrapper(*args, **kwargs):
#         my_loop = loop()
#         future = async_fn(*args, **kwargs)
#         try:
#             result = future.result()
#         except Exception as e:
#             result=False
#             print(e)
#         my_loop.cancel()
#         return result
#     return wrapper

@concurrent.process
def run_cmd(args, ALIVE):
    args.pop(0)
    cmd = " ".join(args) + " > cool.out"
    result = os.system(cmd)
    ALIVE.value = 0
    return result

def cool_matrix_cmd():
    global ALIVE
    future = run_cmd(sys.argv, ALIVE)
    try:
        run_loop()
    except KeyboardInterrupt:
        ALIVE.value = 0
        future.cancel()
    finally:
        sys.exit(0)