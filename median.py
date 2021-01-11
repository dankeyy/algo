""" 
find median from list. if there are is  an odd number of elements- return the middle one. 
if there are an even amount then return the average of the two that sits in the middle. 
for example:
    [2,3,4] -> 3
    [1,2,3,4] -> (2+3)/2 -> 2.5
"""

def median(l: list) -> int:
    around_middle = len(l) // 2

    if len(l) % 2 == 0: return sum(l[around_middle - 1: around_middle + 1]) / 2

    else: return l[around_middle]


if __name__ == "__main__":
    tests = [[2,3], [1,2,3], [1,2,3,4]]
    for test in tests:
        print(median(test))