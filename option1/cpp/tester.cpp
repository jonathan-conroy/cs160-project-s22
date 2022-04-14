#include "hashing_OA.h"
#include "hashing_chaining.h"
#include "hashing_max.h"
#include "hashing_total.h"

#include <iostream>
#include <valgrind/valgrind.h>
#include <cassert>
#include <chrono>

// Note: This code will not run until you implement the methods required
//   by HashtableOA

using namespace std;

int main()
{
    // This code provides a simple test of HashtableOA. Run `make tester`
    // to build the project.
    // 
    // To measure memory:
    // Run
    //     valgrind --tool=massif  --massif-out-file=/dev/null ./hash
    // This will produce two files, snapshot_start.txt and snapshot_end.txt.
    // Look at the `mem_heap_B` value recorded in each file. The difference
    // between these values is the number of bytes required by your hash table.
    // 
    // To measure runtime:
    // Run
    //     ./hash
    // Do NOT use valgrind when measuring runtime, as valgrind has overhead that
    // increases time.

    int toInsert[3] = {1, -2, 10000};

    // Begin timer
    auto starttime = chrono::high_resolution_clock::now();

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
    assert(table->query(1));
    assert(!table->query(235));

    // End timer
    auto endtime = chrono::high_resolution_clock::now();
    double time_taken = chrono::duration_cast<chrono::milliseconds>(endtime - starttime).count();
    cout << "Runtime (ms):  " << time_taken << endl;

    // Free table after the final snapshot
    delete table;
}
