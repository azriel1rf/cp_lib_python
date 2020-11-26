from tiny_algos.mod_arithmetic import permutation, factorial, combination

DEFAULT_MOD = 10 ** 9 + 7


def test_permutation():
    assert permutation(5, 3) == (5 * 4 * 3) % DEFAULT_MOD
    assert permutation(10 ** 10, 1) == (10 ** 10) % DEFAULT_MOD

    assert permutation(1, 1) == 1
    assert permutation(1, 0) == 1
    assert permutation(0, 0) == 1

    mod = 7
    assert permutation(5, 3, mod) == (5 * 4 * 3) % mod
    assert permutation(10 ** 10, 1, mod) == (10 ** 10) % mod

    assert permutation(1, 1, mod) == 1
    assert permutation(1, 0, mod) == 1
    assert permutation(0, 0, mod) == 1


def test_factorial():
    assert factorial(5) == (5 * 4 * 3 * 2 * 1) % DEFAULT_MOD
    assert factorial(DEFAULT_MOD + 1) == 0
    assert factorial(1) == 1
    assert factorial(0) == 1

    mod = 7
    assert factorial(5, mod) == (5 * 4 * 3 * 2 * 1) % mod
    assert factorial(mod + 1, mod) == 0
    assert factorial(1, mod) == 1
    assert factorial(0, mod) == 1


def test_combination():
    assert combination(5, 3) == ((5 * 4 * 3) // (3 * 2 * 1)) % DEFAULT_MOD
    assert combination(10 ** 10, 1) == (10 ** 10) % DEFAULT_MOD

    assert combination(1, 1) == 1
    assert combination(1, 0) == 1
    assert combination(0, 0) == 1

    mod = 2
    assert combination(5, 3, mod) == ((5 * 4 * 3) // (3 * 2 * 1)) % mod
    # denominator might be divided by mod
    assert combination(7, 2, mod) == ((7 * 6) // (2 * 1)) % mod
    mod = 7
    assert combination(10 ** 10, 1, mod) == (10 ** 10) % mod

    assert combination(1, 1, mod) == 1
    assert combination(1, 0, mod) == 1
    assert combination(0, 0, mod) == 1
