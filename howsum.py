from itertools import combinations

""" input is along the lines of (how_sum(7, [2,5,3,200])). needs to return every set of numbers from the given list that sums up to be the given integer (7)"""

def comb(n, l): # an implementation with itertools.combinations
    for i in range(len(l) - 1):
        for c in combinations(l, r=i+1):
            if sum(c) == n:
                yield c                

                
if __name__ == "__main__":
    print(list(comb(7, [4,4,4])))