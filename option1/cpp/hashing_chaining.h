#pragma once

class HashtableChaining {
    public:
        HashtableChaining();
        ~HashtableChaining();
        void insert(int x);
        bool query(int x);
};