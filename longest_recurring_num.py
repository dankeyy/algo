
def longest_recuring(lis: list):

    recurringnum = max_recurringnum = 0
    count = max_count = -1

    for i in range(len(lis) - 1):
        if count > max_count:
            max_recurringnum = recurringnum
            max_count = count
        
        count = (count + 1) if lis[i] == lis[i + 1] else 0
        recurringnum = lis[i]

    max_count += 1 
    return max_recurringnum, max_count

if __name__ == '__main__':
    lis = [1,2,3,3,3,3,4,5,6,7,8,8,8,8,8,8,8,8,8,8]
    print(longest_recuring(lis))