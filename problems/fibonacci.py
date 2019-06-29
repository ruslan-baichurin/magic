# 1. Using memoization method
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fibonacci(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


print(fibonacci(10))

# 2. Using lru_cache decorator
from functools import lru_cache


@lru_cache(maxsize=None)
def fibo_lru(n: int) -> int:
    if n < 2:
        return n
    return fibo_lru(n - 1) + fibo_lru(n - 2)


print(fibo_lru(50))


# 3. Using iterative approach
def fibo_iter(n: int) -> int:
    if n < 1:
        return n
    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, next + last

    return next


print(fibo_iter(50))

# 4. Using a generator
from typing import Generator


def fibo_gen(n: int) -> Generator[int, None, None]:

    yield 0

    if n > 1:
        yield 1

    last, next = 0, 1

    for _ in range(1, n):
        last, next = next, next + last
        yield next


for i in fibo_gen(50):
    print(i)
