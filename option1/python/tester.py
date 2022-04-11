from hashing_OA import Hashtable_OA
from pympler.asizeof import asizeof

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
