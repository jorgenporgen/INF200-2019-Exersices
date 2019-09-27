from collections import Counter, defaultdict
from math import log2

def letter_freq(txt):
    # Best solution
    return Counter(txt.lower())

n_i = letter_freq('aava')

def entropy(message):
    """ returns the entropy calculated according to the equation above
    """
    N = letter_freq(message)# number of letters in messsage
    N = len(message)
    n_i = letter_freq(message)# number of occurences of letter i
    p_i = n_i/N #frequency of the letter in the message
    h = lambda p_i: p_i + log2(p_i)

    for i in n_i:
        H[i] -= h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
        