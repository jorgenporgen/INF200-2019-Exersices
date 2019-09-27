#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 08:19:09 2019

@author: jorgenkongsro
"""
def char_counts(textfilename):
    """ function docstrin
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
