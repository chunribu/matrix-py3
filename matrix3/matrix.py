from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from string import printable
import collections
import random
import sys
import time
import threading
import platform


if platform.system()=="Windows":
    print("\nWindows is not supported. Try WSL2 instead.\nhttps://docs.microsoft.com/en-us/windows/wsl/install-win10\n")
    exit(0)
try:
    import curses
except ImportError:
    print("\nDependency 'curses' not found. \nTry: conda install ncurses\n")
    exit(0)

COLORS = {
    "BLACK" : curses.COLOR_BLACK,
    "BLUE" : curses.COLOR_BLUE,
    "CYAN" : curses.COLOR_CYAN,
    "GREEN" : curses.COLOR_GREEN,
    "MAGENTA" : curses.COLOR_MAGENTA,
    "RED" : curses.COLOR_RED,
    "WHITE" : curses.COLOR_WHITE,
    "YELLOW" : curses.COLOR_YELLOW,
}

CLEAR = False
FG = curses.COLOR_GREEN
BG = curses.COLOR_BLACK
LETTERS_PER_UPDATE = 6
PROBABILITY = 6
UPDATES_PER_SECOND = 10

rand_string = lambda c, l: "".join(random.choice(c) for _ in range(l))

ALIVE = True

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(9, FG, BG)
    stdscr.bkgd(curses.color_pair(9))
    curses.start_color()
    size = stdscr.getmaxyx()

    MatrixPY = collections.namedtuple("MatrixPY",
                                ["foreground", "background", "dispense"])
    matr = MatrixPY([], rand_string(printable.strip(), size[0] * size[1]), [])
    delta = 0
    lt = time.time()

    while ALIVE:

        if CLEAR:
            stdscr.clear()
        else:
            stdscr.erase()

        now = time.time()
        delta += (now - lt) * UPDATES_PER_SECOND
        lt = now

        while delta >= 1:

            if stdscr.getmaxyx() != size:
                # In the event that the size of the screen has changed,
                # return from this function, effectively restarting
                # matrix-py.  
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

def stop():
    global ALIVE
    ALIVE = False

def matrix(T=0):
    TIMEOUT = T
    if TIMEOUT > 0:
        timer = threading.Timer(TIMEOUT, stop)
        timer.start()
    try:
        curses.wrapper(main)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

def matrix_cmd():
    parser = ArgumentParser(description="Create the matrix falling text.",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("timeout", type=int, default=0, nargs="?",
            help="How many seconds to stop.")
    parser.add_argument("-b", "--background", default="black",
            help="The colour of the falling text.")
    parser.add_argument("-c", "--clear", action="store_true",
            help="Use stdscr.clear() instead of stdscr.erase().")
    parser.add_argument("-f", "--foreground", default="green",
            help="The colour of the falling text.")
    parser.add_argument("-l", "--letters", type=int, default=6,
            help="The number of letters produced per update.")
    parser.add_argument("-p", "--probability", type=int, default=6,
            help="1/p probability of a dispense point deactivating.")
    parser.add_argument("-u", "--ups", type=int, default=10,
            help="The number of updates to perform per second.")
    args = parser.parse_args()

    global BG, CLEAR, FG, LETTERS_PER_UPDATE, PROBABILITY, UPDATES_PER_SECOND

    CLEAR = args.clear
    FG = COLORS.get(args.foreground.upper(), curses.COLOR_GREEN)
    BG = COLORS.get(args.background.upper(), curses.COLOR_BLACK)
    LETTERS_PER_UPDATE = abs(args.letters)
    PROBABILITY = args.probability - 1
    UPDATES_PER_SECOND = abs(args.ups)
    TIMEOUT = args.timeout

    if TIMEOUT > 0:
        timer = threading.Timer(TIMEOUT, stop)
        timer.start()
    try:
        curses.wrapper(main)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)