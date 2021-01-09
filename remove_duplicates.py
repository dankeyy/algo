""" given a sorted array of integers. remove duplicates from the list by modifying it (with no extra helper array) and return the length of it once it's fixed""" 

def removeDuplicates(nums : list) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]: del nums[i]
        else: i += 1

    return len(nums)


if __name__ == "__main__":
    tests = [[1,2,2,2,3,4,5], [4,5,7,8,8,8,8,8,8,8], [1,1,2,3,4,5]]
    for test in tests:
        print(removeDuplicates(test), test, sep='-->')