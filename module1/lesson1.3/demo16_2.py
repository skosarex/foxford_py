def F(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = F(n - 1) * n + F(n - 2) * (n - 1)
    return result


print(F(7))
