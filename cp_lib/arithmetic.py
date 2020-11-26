DEFAULT_MOD = 10 ** 9 + 7


def permutation(n, k, mod=DEFAULT_MOD):
    ret = 1
    for i in range(n, n - k, -1):
        ret = (ret * i) % mod
    return ret


def factorial(n, mod=DEFAULT_MOD):
    return permutation(n, n)


def combination(n, k, mod=DEFAULT_MOD):
    k = min(k, n - k)
    numerator = permutation(n, k)
    denominator = factorial(k)
    return numerator * pow(denominator, mod - 2, mod)
