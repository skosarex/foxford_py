def F(n):
    if n == 1:
        result = 1
    else:
        result = 3 * F(n - 1) + 2 + n
    return result


print(F(3))
