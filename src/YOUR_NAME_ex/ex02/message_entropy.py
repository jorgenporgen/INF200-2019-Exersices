""" This module is part of the ex_02 assignment """

from collections import Counter
from math import log2


def letter_freq(txt):
    """ Function from ex_01
    Returns:
        Counter: dict
    """
    return Counter(txt.lower())

n_i = letter_freq('aava')


def entropy(message):
    """ returns the entropy calculated according to the equation above
    Returns:
        H: list
    """
    N = len(message) # number of letters in message
    n_i = letter_freq(message) # number of occurences of letter i
    code_points = [ord(character) for character in message] # get code_points
    p_i = [n_i[chr(code_point)]/N for code_point in code_points]

    # Calculate entropy. I was not successfull in calculating entropy
    H = []
    h = lambda p_i: p_i + log2(p_i)
    for i in p_i:
        H -= h
    return H


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
        