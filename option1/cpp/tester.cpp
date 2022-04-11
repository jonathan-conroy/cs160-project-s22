#include "hashing_OA.h"
#include "hashing_chaining.h"
#include "hashing_max.h"
#include "hashing_total.h"

#include <iostream>
#include <valgrind/valgrind.h>

// Note: This code will not run until you implement the methods required
//   by HashtableOA

using namespace std;

int main()
{
    // This code provides a simple test of HashtableOA and contains
    // instructions for measuring its memory usage.
    // 
    // Run `make tester`, then run
    //     valgrind --tool=massif  --massif-out-file=/dev/null ./hash
    // This will produce two files, snapshot_start.txt and snapshot_end.txt.
    // Look at the `mem_heap_B` value recorded in each file. The difference
    // between these values is the number of bytes required by your hash table.
    // 

    int toInsert[3] = {1, -2, 10000};

    // Record heap size before allocation
    // (Do not forget to include "valgrind.h" above)
    VALGRIND_MONITOR_COMMAND("snapshot snapshot_start.txt");

    // Allocate a hash table using the "new" keyword
    HashtableOA* table = new HashtableOA();

    for (size_t i = 0; i < 3; i++)
    {
        table->insert(toInsert[i]);
    }

    // Record heap size after allocation and insertions
    VALGRIND_MONITOR_COMMAND("snapshot snapshot_end.txt"); 
    
    // Execute queries after the final snapshot
    cout << "Expected TRUE, got: " << table->query(1) << endl;
    cout << "Expected FALSE, got: " << table->query(235) << endl;

    // Free table after the final snapshot
    delete table;
}
