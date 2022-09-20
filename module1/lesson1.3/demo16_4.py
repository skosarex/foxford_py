def F(n):
    print('*')
    if n >= 1:
        print('*')
        F(n - 1)
        F(n - 2)


def f(n):
    if n < 1:
        return 1
    else:
        return 2 + f(n - 1) + f(n - 2)


print(f(28))
