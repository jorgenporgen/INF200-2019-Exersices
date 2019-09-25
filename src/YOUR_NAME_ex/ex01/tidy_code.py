# -*- coding: utf-8 -*-
"""
This is a guess game. Have fun and guess a number between 1 and 10.
You will have 3 attempts. Number of points will be based on number of attempts.

Attributes:
    guess_number (int) = guess a number bewtween 1 and 10

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


def reference_number():
    """
    Select a number from a random distribution between 1 and 10
    Attributes:
        number (int)
    """
    return select_rand(1, 10)


def correspondence(number, reference_number):
    """
    Check correspndence between guessed number and reference number
    Attibutes:
        number (int)
        reference_number (int)
    """
    return number == reference_number


def play_game():
    """
    Play a single game of guess number
    Returns
    -------
    game_result: bool
        True if the game resulted in a win and False otherwise.
    """
    game_result = False
    attempts = 3
    j = reference_number()
    while not game_result and attempts > 0:
        k = guess_number()
        game_result = correspondence(j, k)
        if not game_result:
            print('Wrong, try again!')
            attempts -= 1

    if attempts > 0:
        print('You won {} points.'.format(attempts))
    else:
        print('You lost. Correct answer: {}.'.format(j))


play_game()
