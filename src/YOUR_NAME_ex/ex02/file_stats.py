
def char_counts(filename):
    """ Count how often each character code (0–255) occurs in the string
    
    Returns
    -------
    result: list or tuple
    """
    
    return

if __name__ == '__main__':
    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)
                print('{:3}{:>4}{:6}'.format(
                        code, character, frequencies[code]
                        )
    )
