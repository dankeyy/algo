"""https://t.me/prograchallenges/432 -find the number of boomerangs in a list"""


valid_triplet = lambda x: x[0] == x[2] != x[1]

boomerang = lambda x: sum(valid_triplet(x[i:i+3]) for i in range(len(x) - 2))


if __name__ == '__main__':
    tests = [[3, 7, 3, 2, 1, 5, 1, 2, 2, -2, 2], [9, 5, 9, 5, 1, 1, 1], [5, 6, 6, 7, 6, 3, 9], [4, 4, 4, 9, 9, 9, 9]]

    print(*(boomerang(t) for t in tests))