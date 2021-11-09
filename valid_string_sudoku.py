from itertools import product

mul3 = ((3).__mul__)


def fields(s):
    m = [s[i:i+9] for i in range(0, len(s), 9)]

    for i in range(9):
        yield s[i :: 9] # columns # or- m[x][i] for x in range(len(grid))
        yield m[i] # rows # or- s[i*9 : (i+1) * 9]

        x0, y0 = map(mul3, divmod(i, 3))
        yield [m[x0+x][y0+y] for x, y in product(range(3), repeat=2)] # maybe as gen/ set comp instead idk


def valid_sudoku(s):
    return all(len(set(f)) == 9 for f in fields(s))

# valid board for testing
test = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'
print(valid_sudoku(test))
