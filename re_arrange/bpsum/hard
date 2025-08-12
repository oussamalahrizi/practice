#!/usr/bin/python3

import sys
import itertools

def getMaxBeauty(nums : list[int]):
    
    nums.sort(reverse=True)
    l, r = 0, len(nums) - 1
    result = []
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(nums[l])
            l += 1
        else:
            result.append(nums[r])
            r -= 1
    print(nums)
    print(result)
    prefix = list(itertools.accumulate(result))
    print(prefix)
    res = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            res += prefix[i]
        else:
            res -= prefix[i]
    
    return res



"""
    [3, 4, 5, 1, 1]
    [3, 7, 12, 13, 14]
    
    
"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error azby", file=sys.stderr)
        sys.exit(1)
    arr = sys.argv[1].split(' ')
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    print(getMaxBeauty(arr))
