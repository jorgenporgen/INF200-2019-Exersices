# -*- coding: utf-8 -*-
"""
This is a guess game. Have fun and guess a number between 0 and 9

Attributes:
    guess_number (int) = guess a number bewtween 0 and 9

"""
from random import randint as select_rand

__author__ = 'Jørgen Kongsro'
__email__ = "jorjoh@nmbu.no"


def guess_number():
    """
    Guess a number
    Attributes:
        number (int)
    """

    number = 0
    while number < 1:
        number = int(input('Your guess: '))
    return number


def selected_number():
    """
    DOCSTRING
    """
    return select_rand(1, 6) + select_rand(1, 6)


def equal_numbers(f, g):
    """
    DOCSTRING
    """
    return f == g


if __name__ == '__main__':
    h = False
    ATTEMPTS = 3
    j = selected_number()
    while not h and ATTEMPTS > 0:
        k = guess_number()
        h = e(j, k)
        if not h:
            print('Wrong, try again!')
            ATTEMPTS -= 1

    if ATTEMPTS > 0:
        print('You won {} points.'.format(ATTEMPTS))
    else:
        print('You lost. Correct answer: {}.'.format(j))
        