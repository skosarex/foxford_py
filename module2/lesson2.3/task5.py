for d1 in range(1, 10):
    for d2 in range(10):
        for d3 in range(10):
            for d4 in range(10):
                trash, b, c = sorted([d1 + d2, d2 + d3, d3 + d4])
                if b == 5 and c == 11:
                    print(d1, d2, d3, d4)
