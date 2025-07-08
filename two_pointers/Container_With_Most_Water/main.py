#!/usr/bin/env python3

"""
    medium
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxx = 0
        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            if current > maxx:
                maxx = current
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return maxx



if __name__ == '__main__':
    s = Solution()

    tests = [
        [1,7,2,5,4,7,3,6],
        [2,2,2]
    ]
    for e in tests:
        r = s.maxArea(e)
        print(r)