def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    k = []
    for k in range(n):
        if k % 3 == 1:
            k ** 2
        k.append(n)
    return k
