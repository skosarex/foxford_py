from functools import lru_cache

@lru_cache
def F(n):
    if n <= 5:
        result = 2 * n
    elif n % 2 == 0:
        result = F(n - 2) + 2 * F(n / 2) - n
    else:
        result = F(n - 1) + F(n - 2) + n
    return result


print(F(79) + F(98))
