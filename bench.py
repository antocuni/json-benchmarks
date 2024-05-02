import sys
import time
import ujson

N = 50

def load(fname):
    s = open(fname).read()
    a = time.time()
    for i in range(N):
        data = ujson.loads(s)
    b = time.time()
    print(f'load  : {b-a:.4f} seconds')

def dump(fname):
    s = open(fname).read()
    f = open('/dev/null', 'w')
    data = ujson.loads(s)

    a = time.time()
    for i in range(N):
        ujson.dump(data, f)
    b = time.time()
    print(f'dump  : {b-a:.4f} seconds')

def both(fname):
    a = time.time()
    load(fname)
    dump(fname)
    b = time.time()
    print(f'total : {b-a:.4f} seconds')

def usage():
    print('Usage: bench.py FILENAME [load|dump|both]')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        fname = sys.argv[1]
        what = sys.argv[2]
    elif len(sys.argv) == 2:
        fname = sys.argv[1]
        what = 'both'
    else:
        usage()

    if what == 'load':
        load(fname)
    elif what == 'dump':
        dump(fname)
    elif what == 'both':
        both(fname)
    else:
        usage()
