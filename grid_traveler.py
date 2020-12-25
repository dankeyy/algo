from functools import lru_cache

""" how many possible paths are there take for one to go from the top left of a X by Y grid-
    to the bottom right taking steps only downwards or right? """

@lru_cache
def travel(x, y):
    if 0 in {x, y}: return 0
    if 1 in {x, y}: return 1
    return travel(x, y - 1) + travel(x - 1, y)

if __name__ == "__main__":
    print( travel(100,100) )