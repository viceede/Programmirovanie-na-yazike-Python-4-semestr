from functools import lru_cache


def main(n):
    @lru_cache(None)
    def f(n):
        if n == 0:
            return -0.70
        elif n == 1:
            return 0.38
        return 1 - f(n - 1) - f(n - 2) ** 3

    return f(n)