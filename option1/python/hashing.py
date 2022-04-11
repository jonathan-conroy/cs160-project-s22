from cgitb import small
import numpy as np
from collections import Counter
import linecache
import os
import tracemalloc
import sys
from pympler.asizeof import asizeof
import numpy

TABLE_SIZE = 100000
memory = [-1 for _ in range(TABLE_SIZE)]

def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


class HashTableOA:
    def __init__(self):
        # TODO: Constructor
        self.TABLE_SIZE = 10000
        self.memory = np.array([-10000 for _ in range(self.TABLE_SIZE)])
    
    def insert(self, x):
        # TODO: Insert
        k = 0
        inserted = False
        while (not inserted):
            inserted = self._insert_iter(x, k)
            k += 1
        return None

    def _insert_iter(self, x, k):
        index = (x + k) % self.TABLE_SIZE
        if self.memory[index] == -10000:
            self.memory[index] = x
            return True
        else:
            return False

    
    def query(self, x):
        # TODO: Query
        k = 0
        while True:
            index = (x + k) % self.TABLE_SIZE
            if self.memory[index] == x:
                return True
            elif self.memory[index] != -10000:
                k += 1
            else:
                return False


def smallTest():
    table = HashTableOA()
    for i in range(10000):
        table.insert(i)
    # assert(table.query(10) is True)
    # assert(table.query(5) is True)
    print("All tests passed!")
    print("table size:", asizeof(table.memory) * 0.000976562, "KiB")
    print("table dtype:", type(table.memory))



smallTest()

print("-------")
print("-------")

tracemalloc.start()
a = np.array([x for x in range(10000)], dtype=object)
snapshot = tracemalloc.take_snapshot()
# display_top(snapshot)
print("a size:", asizeof(a) * 0.000976562, "KiB")
b = np.array([i for i in range(10000)])
snapshot = tracemalloc.take_snapshot()
# display_top(snapshot)
print("b size:", asizeof(b) * 0.000976562, "KiB")

c = list(range(10000))
print("c size:", asizeof(c) * 0.000976562, "KiB")


# def insert(x):
#     k = 0
#     inserted = False
#     while (not inserted):
#         inserted = insert_iter(x, k)
#         k += 1

# def insert_iter(x, k):
#     k = 0
#     inserted = False
#     while (not inserted):
#         inserted = insert_iter(x, k)
#         k += 1


# def test():
#     to_insert = np.random.randint(1, 2147483640, size = 500000)
#     for x in to_insert:
#         insert(x)
#     print("inserted!")

# tracemalloc.start()
# TABLE_SIZE = 50000
# memory = [-1 for _ in range(TABLE_SIZE)]
# snapshot = tracemalloc.take_snapshot()
# display_top(snapshot)


# import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)