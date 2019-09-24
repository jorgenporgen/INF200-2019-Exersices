

from random import randint as a

__author__ = 'Jørgen Kongsro'
__email__ = "jorjoh@nmbu.no"

class guess:
    """
    Create a guessing game selecting a number between 0 and 9. 
    You will have three attempts
    
    
    """
    def __init__(self, r):
        self.c = c
        self.f = f
        self.g = g


    def inputguess(self):
        guess_number = 0
        while guess_number < 1:
            guess_number = int(input('Your guess: '))
        return guess_number
    
    
    def d():
        return a(1, 6) + a(1, 6)
    
    
    def e(f, g):
        return f == g


if __name__ == '__main__':
    print('This is a guess game. Have fun and guess a number between 0 and 9'
          'You can guess 3 times, and the number of points will be based on the number of guesses')
    h = False
    i = 3
    j = d()
    while not h and i > 0:
        k = b()
        h = e(j, k)
        if not h:
            print('Wrong, try again!')
            i -= 1

    if i > 0:
        print('You won {} points.'.format(i))
    else:
        print('You lost. Correct answer: {}.'.format(j))