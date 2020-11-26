from cp_lib.arithmetic import permutation, factorial, combination

DEFAULT_MOD = 10 ** 9 + 7


def test_permutation():
    assert permutation(5, 3) == (5 * 4 * 3) % DEFAULT_MOD
    assert permutation(5, 1) == 5 % DEFAULT_MOD
    assert permutation(5, 0) == 1

    assert permutation(1, 1) == 1
    assert permutation(1, 0) == 1
    assert permutation(0, 0) == 1

    mod = 7
    assert permutation(10, 2, mod) == (10 * 9) % mod
    assert permutation(10, 1, mod) == 10 % mod
    assert permutation(10, 0, mod) == 1


def test_factorial():
    assert factorial(4) == (4 * 3 * 2 * 1) % DEFAULT_MOD
    assert factorial(1) == 1
    assert factorial(0) == 1

    mod = 7
    assert factorial(4, mod) == (4 * 3 * 2 * 1) % mod
    assert factorial(1, mod) == 1
    assert factorial(0, mod) == 1


def test_combination():
    assert combination(5, 3) == ((5 * 4 * 3) // (3 * 2 * 1)) % DEFAULT_MOD
    assert combination(5, 1) == 5
    assert combination(5, 0) == 1

    assert combination(1, 1) == 1
    assert combination(1, 0) == 1
    assert combination(0, 0) == 1

    mod = 7
    assert combination(10, 3, mod) == ((10 * 9 * 8) // (3 * 2 * 1)) % mod
    assert combination(10, 1, mod) == 10 % mod
    assert combination(10, 0, mod) == 1
