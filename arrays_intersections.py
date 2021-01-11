"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

"""

def intersect(nums1, nums2):
    def inner():
        for x in set(nums1) & set(nums2):
            for m in range( min(nums1.count(x), nums2.count(x)) ):
                yield x
                
    return list(inner())

if __name__ == "__main__":
    tests = (
        ( [1,2,2,1], [2,2] ),
        ( [4,9,5], [9,4,9,8,4] )

    )

    for test in tests:
        print(f'{test = }\nanswer=', intersect(*test), end='\n\n')