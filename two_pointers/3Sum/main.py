#!/usr/bin/env python3

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
            i + j + k = 0
            i + j = -k
        """
        result = []
        nums.sort()
        index = 0
        while index < len(nums) - 2:
            target = -nums[index]
            left = index + 1
            right = len(nums) - 1
            while left < right:
                current = nums[left] + nums[right]
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    tmp = [nums[index], nums[left], nums[right]]
                    tmp.sort()
                    if tmp not in result:
                        result.append(tmp)
                    left += 1
            index += 1
        return result


if __name__ == '__main__':

    tests = [
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [-2,0,1,1,2]
    ]
    for e in tests:
        r = Solution().threeSum(e)
        print(r)