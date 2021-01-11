from itertools import chain

def rotate1(nums, k):
    l= len(nums)
    return nums[l - k::] + nums[:l - k:]


def rotate2(nums, k):
    l= len(nums)
    start, end = range(0, l - k), range(l - k, l)
    return [nums[i] for i in chain(end, start)]


def rotate3(nums, k):
    l= len(nums)
    def inner():
        for i in range(l - k, l): yield nums[i]
        for i in range(0, l-k): yield nums[i]
    return list(inner())


rotators = rotate1, rotate2, rotate3

if __name__ == "__main__":
    tests = (
        ([9,8,7,6,5,4,3,2,1], 1),
        ([-1,-100,3,99], 2),
        ([1,2,3,4,5,6,7], 3),
        ([-333, -444, 555, 666, 2, 3, 88, 77], 4),
    )

    for j, rotator in enumerate(rotators, 1):
        for i, test in enumerate(tests, 1):
            print(f'test #{i} -> {test},  \nrotator #{j} result for test #{i} -> {rotator(*test)}', end='\n\n')
        print('\n')