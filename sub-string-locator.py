from itertools import permutations
import re
from collections import defaultdict

"""A script to find indexes of all k-lengthed substrings in a given string.
   for example, output for ('aabbaa', 2) should be {'aa': [0, 4], 'ab': [1], 'bb': [2], 'ba': [3]}"""


def bad_dontuseit(s: str, k: int) -> dict: # k stands for the length of the desired substring
    
    substrings = set( st for x in permutations(s, k) if (st := ''.join(x)) in s )  # all non repeating permutations of s that are substrings in it
    dic = {}

    for string in substrings:
        dic[string] = [m.start() for m in re.finditer(string, s)] # a list of indexes marking occurences of a substring in s

    return {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])} # if you need it by order. if not just return dic


def subfinder(s, k):
    dic = defaultdict(list)
    values = (s[i: i + k] for i in range(len(s) - k - 1))
 
    for i, v in enumerate(values): dic[v].append(i)
 
    return dict(dic)
 

if __name__ == '__main__':
    print(subfinder('TTAATTAGGGGCGC', 2))
