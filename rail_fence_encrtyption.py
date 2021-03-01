""" 
    This is my pretty verbose implementation of a rail fence cipher encoding & decoding.
    Wikipedia: https://en.wikipedia.org/wiki/Rail_fence_cipher
    Challenge link at codewars: https://www.codewars.com/kata/58c5577d61aefcf3ff000081
"""

from itertools import product


def travel_and_set(text, key, mark=None, getmode=False, input_grid=None): 
    """ travels in zig-zag and sets a letter/mark or rather gets a letter/mark from the corresponding cells"""

    down = False 
    grid = [[None for _ in range(len(text))] for _ in range(key)] if not getmode else input_grid
    row = 0
    if getmode: cipher = []
 

    for col in range(len(text)):
        if getmode: cipher.append(grid[row][col])
        else: grid[row][col] = text[col] if mark is None else mark
        

        if row in {0, key-1}: down = not down
        row += 1 if down else -1


    return cipher if getmode else grid



def encrypt(text, key):
    grid = travel_and_set(text, key) # sprinkling text in zig zag over the grid

    return ''.join( letter for row, col in product( range(key), range(len(text)) )
                    if (letter := grid[row][col]) is not None ) # collecting encrypted text by iterating regularly over the grid



def decrypt(text, key):
    grid = travel_and_set(text, key, mark='#') # setting zig zag marks over an empty grid sized by text length and key

    i = 0 # traveling regularly to transform zig zag marks to cipher characters
    for row in range(key):
        for col in range(len(text)):
            if grid[row][col] == '#':
                grid[row][col] = text[i]
                i += 1

    return ''.join(travel_and_set(text, key, getmode=True, input_grid=grid)) # collecting previously set characters by iterating in zig zag form




print(encrypt('WEAREDISCOVEREDFLEEATONCE', 3))
print(decrypt('WECRLTEERDSOEEFEAOCAIVDEN', 3))