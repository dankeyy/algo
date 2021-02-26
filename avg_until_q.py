
""" 
    So this is a relatively simple exercise for beginners to learn assignments, arithmetic operations and simple I/O.
    What this is trying to do is to take a different approach to this problem using a small generator function and a mapping.
    Perhaps could be done with count and/or takewhile, but that's a task for another day.

"""

from operator import truediv
from itertools import takewhile, count


def avg1():
    def calc():
        while (inp := input('numpls> ')):
            yield int(inp), 1

    return truediv(
                *tuple(
                    map(sum, zip( *calc() )) 
                )
           )
                            

if __name__ == '__main__':
    print(avg1())