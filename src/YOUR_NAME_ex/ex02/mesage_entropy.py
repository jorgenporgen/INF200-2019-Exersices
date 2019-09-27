from collections import Counter, defaultdict

def letter_freq(txt):
    # Best solution
    return Counter(txt.lower())


def entropy(message):
    """ returns the entropy calculated according to the equation above
    """
    N = letter_freq(message)# number of letters in messsage
    n_i # number of occurences of letter i (i is the UTF-8 code for the letter)
    p_i = n_i/N #frequency of the letter in the message
    
    H = - \sum_i p_i \log_2 p_i


   if __name__ == "__main__":
       for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
           print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))