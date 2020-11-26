from tiny_algos.mod_arithmetic import (
    mod_permutation,
    mod_factorial,
    mod_combination,
)

DEFAULT_MOD = 10 ** 9 + 7


def test_permutation():
    assert mod_permutation(5, 3) == (5 * 4 * 3) % DEFAULT_MOD
    assert mod_permutation(10 ** 10, 1) == (10 ** 10) % DEFAULT_MOD

    assert mod_permutation(1, 1) == 1
    assert mod_permutation(1, 0) == 1
    assert mod_permutation(0, 0) == 1

    mod = 7
    assert mod_permutation(5, 3, mod) == (5 * 4 * 3) % mod
    assert mod_permutation(10 ** 10, 1, mod) == (10 ** 10) % mod

    assert mod_permutation(1, 1, mod) == 1
    assert mod_permutation(1, 0, mod) == 1
    assert mod_permutation(0, 0, mod) == 1


def test_factorial():
    assert mod_factorial(5) == (5 * 4 * 3 * 2 * 1) % DEFAULT_MOD
    assert mod_factorial(DEFAULT_MOD + 1) == 0
    assert mod_factorial(1) == 1
    assert mod_factorial(0) == 1

    mod = 7
    assert mod_factorial(5, mod) == (5 * 4 * 3 * 2 * 1) % mod
    assert mod_factorial(mod + 1, mod) == 0
    assert mod_factorial(1, mod) == 1
    assert mod_factorial(0, mod) == 1


def test_combination():
    assert mod_combination(5, 3) == ((5 * 4 * 3) // (3 * 2 * 1)) % DEFAULT_MOD
    assert mod_combination(10 ** 10, 1) == (10 ** 10) % DEFAULT_MOD

    assert mod_combination(1, 1) == 1
    assert mod_combination(1, 0) == 1
    assert mod_combination(0, 0) == 1

    mod = 2
    assert mod_combination(5, 3, mod) == ((5 * 4 * 3) // (3 * 2 * 1)) % mod
    # denominator might be divided by mod
    assert mod_combination(7, 2, mod) == ((7 * 6) // (2 * 1)) % mod
    mod = 7
    assert mod_combination(10 ** 10, 1, mod) == (10 ** 10) % mod

    assert mod_combination(1, 1, mod) == 1
    assert mod_combination(1, 0, mod) == 1
    assert mod_combination(0, 0, mod) == 1
