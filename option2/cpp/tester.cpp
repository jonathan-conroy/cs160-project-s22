#include "implement_hw.h"
#include <vector>
#include <iostream>

using namespace std;

// Note: this code will error unless you implement the methods in implement_hw.h

void testMagicStones(){
    vector<int> stones{1, 4, 6, 11, 25};
    int health = 228;
    int scoreBottomup = magicStonesBottomup(stones, health);
    int scoreTopdown = magicStonesTopdown(stones, health);
    cout << "Min stones should be 11." << endl;
    cout << "Min stones, computed bottom-up: " << scoreBottomup << endl;
    cout << "Min stones, computed top-down: " << scoreTopdown << endl;
}

void testCountFlips(){
    vector<int> arr{4, 1, 2, 1};
    int flips = countFlips(arr);
    cout << "Number of flips should be 4 and is " << flips << endl;
}


int main(){
    testMagicStones();
    cout << "-----" << endl;
    testCountFlips();
}
