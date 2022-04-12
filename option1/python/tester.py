from hashing_OA import Hashtable_OA
from pympler.asizeof import asizeof

# Note: Please do NOT use numpy. The pympler "asizeof" method that we recommend
#       using to calculate memory usage does not work well with numpy arrays.
# Note: Python memory management is weird: the array [1, 2, 3, 4, 5] takes more
#       space than the array [1, 1, 1, 1, 1]. This is because Python arrays
#       actually store pointers to the values, rather than the values
#       themselves; the int "1" can be reused in the former case, while
#       5 distinct ints need to be created in the latter case.
#       **This phenomenon should affect chaining and open addressing
#       in roughly the same way, so you should be able to safely ignore it.**
#       If you want more control over memory usage, use C++ instead...

# A small test demonstrating expected behavior
def smallTest(table):
    for x in [1, -2, 10000]:
        table.insert(x)
    assert(table.query(1) is True)
    assert(table.query(235) is False)
    print("All tests passed!")
    print("Table Size:", asizeof(table.memory) / 1024, "KiB")

if __name__ == "__main__":
    print("-----------------")
    print("Testing Open Addressing")
    table_oa = Hashtable_OA()
    smallTest(table_oa)
    print("-----------------")
