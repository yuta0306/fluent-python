import bisect
import random
import sys

import timeit

SIZE = 7

random.seed(1729)

mylist = []

def insorted(SIZE):
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(mylist, new_item)
        print(f'{new_item:2d} -> {mylist}')

TIMES = 10
SETUP = """
import bisect
import random

random.seed(1729)

mylist = []

def insorted(SIZE):
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(mylist, new_item)
        # print(f'{new_item:2d} -> {mylist}')
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

if __name__ == "__main__":
    if sys.argv[-1] == 'speed':
        clock('bisect.insort    :', 'insorted(1000)')
        clock('listcomp & sorted:', 'mylist = [random.randrange(1000 * 2) for _ in range(1000)]\nmylist = sorted(mylist)')
    else:
        for i in range(SIZE):
            new_item = random.randrange(SIZE * 2)
            bisect.insort(mylist, new_item)
            print(f'{new_item:2d} -> {mylist}')