
from operator import itemgetter

def longest_incresing_subseq(x):

    longest = initiated = 0
    s_table = (x[i+1] - x[i] == 1 for i in range(len(x) - 1))

    for i, successor in enumerate(s_table):
        if successor: 
            longest += 1
            if not initiated: initiated = i

            if i != len(x) - 2: 
                continue # if the current element is a successor, don't bother yielding unless its the last element 
    
        if initiated: 
            yield longest + 1, initiated
            longest = initiated = 0


x = [7,6,9,10,11,15,16,12,5,6,7,8,9,7,2,3,4]
print(max(longest_incresing_subseq(x), key=itemgetter(0)))

# max_length, starting_at = 
# print(f'{max_length=}, {starting_at=}') 

# [(0, False), (1, False), (2, True), (3, True), (4, False), (5, True), (6, False), (7, False), (8, True), (9, True), 
# (10, True), (11, True), (12, False), (13, False), (14, True), (15, True), (16, True), (17, True), (18, True)]