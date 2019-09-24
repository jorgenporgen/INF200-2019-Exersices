def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    deck = []
    for k in range(n):
        if k % 3 == 1:
            deck.append(k ** 2)
    return deck


if __name__ == '__main__':
    n = 2
    if squares_by_comp(n) != squares_by_loop(n):
        print('ERROR!')
