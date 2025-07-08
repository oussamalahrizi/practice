#!/usr/bin/env python3

"""
    hard

    two pointers is pretty hard (skill issue actually)
    just use prefix left max and postfix right max
    
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        pass


if __name__ == '__main__':
    s = Solution()

    tests = [
       [0,2,0,3,1,0,1,3,2,1]
    ]
    for e in tests:
        r = s.twoSum(e)
        print(r)