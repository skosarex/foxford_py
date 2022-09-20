def F(n):
    if n <= 1:
        return 3 * n
    else:
        return 3 * n + n - 2 + F(n - 1) + F(n - 2)


for n in range(1, 1000):
    print(n, F(n))
