
from typing import List
from operator import itemgetter
import numpy as np

def snail(m: List[List[int]]) -> List[int]:
    s = [] # sorted snail

    while 1:
        try:
            s.extend(m.pop(0)) # top row

            s.extend(m[i].pop(-1) for i in range(len(m))) # right col

            s.extend(reversed(m.pop(-1))) # bottom row

            s.extend(m[i].pop(0) for i in range(len(m)-1, 0, -1)) # left col


        except IndexError: break

    return s


def np_snail(m):
    snail = np.empty(0)

    while m.size:
        snail = np.concatenate((snail, m[:1]), axis=None)
        m = np.rot90(m[1:])

    return snail


if __name__ == "__main__":
    x = [[1,2,3], [8, 9, 4], [7,6, 5]]
    print(snail2(np.array(x)))