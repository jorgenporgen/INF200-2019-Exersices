def char_counts(filename):
    """ opens the file with the given 'filename' using encoding 'utf-8' and 
    reads the entire file content into a single string the file and count 
    how often each character code (0–255) occurs in the string

    Returns
    -------
    result: list or tuple
    """
    check_string = open(filename, encoding='utf8').read()
    result = [0] * 256
    for ch in check_string:
        i = ord(ch)    
        result[i] += 1

    return result

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
                        ))