def letter_freq(txt):
    # using dict.get() to get count
    # of each element in string
    frequencies = {}

    for keys in txt:
        frequencies[keys] = frequencies.get(keys, 0) + 1

    return frequencies


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
