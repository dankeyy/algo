from itertools import product

def is_sudoku_correct(solved_sudoku: str):
    """recieves an 81-character long string and determines if it represents a valid sudoku"""

    grid = [solved_sudoku[i: i + 9] for i in range(0, len(solved_sudoku), 9)]

    def valid_fields():
        for i, row in enumerate(grid):
            for j in range(len(row)):
                current_row = set(row)
                current_column = {grid[x][j] for x in range(len(grid))}

                x0 = (i // 3) * 3
                y0 = (j // 3) * 3
                current_square = {grid[x0 + x][y0 + y] for x, y in product(range(3), repeat=2)}

                yield all(len(field) == 9 for field in (current_row, current_column, current_square))

    return all(valid_fields())

# should print True
print(is_sudoku_correct('864371259325849761971265843436192587198657432257483916689734125713528694542916378'))
