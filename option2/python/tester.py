from implement_hw import magic_stones_topdown, magic_stones_bottomup, count_flips

if __name__ == "__main__":
    # Test "magic stones" problem
    stones = [1, 4, 6, 11, 25]
    health = 228
    assert(magic_stones_topdown(stones, health) == 11)
    assert(magic_stones_bottomup(stones, health) == 11)

    # Test "count flips" problem
    arr = [4, 1, 2, 1]
    assert(count_flips(arr) == 4)