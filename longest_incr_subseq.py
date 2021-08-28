
from operator import itemgetter

def longest_incresing_subseq(x):
    "finding the longest subsequence of increasing & following elements in the list, returning the length of that subseq along with its first index"
    
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
# outputs (5 -length, 8 - starting index) because 5,6,7,8,9 is the longest increasing subseq, starting from 8 with a length of 5 
