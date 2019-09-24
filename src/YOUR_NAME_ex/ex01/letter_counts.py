def letter_freq(txt):
    # using dictonary approach to get count
    # of each element in string
    freqs = {}

    for keys in txt:
        freqs[keys] = freqs.get(keys, 0) + 1

    return freqs


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
