def fibo_iter(n: int) -> int:
    if n < 2:
        return n

    last, next = 0, 1

    for _ in range(1, n):
        last, next = next, next + last

    return next


def fibo_naive(n: int) -> int:
    if n < 2:
        return n

    return fibo_naive(n - 1) + fibo_naive(n - 2)


from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fibo_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)

    return memo[n]

from functools import lru_cache

@lru_cache(maxsize=None)
def fibo_lru(n: int) -> int:
    if n < 2:
        return n
    return fibo_lru(n - 1) + fibo_lru(n - 2)


print(fibo_lru(200))


