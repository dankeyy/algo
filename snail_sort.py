
from typing import List


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


if __name__ == "__main__":
    x = [[1,2,3], [8, 9, 4], [7,6, 5]]
    print(snail(x))