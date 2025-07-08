#!/usr/bin/env python3

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left + 1, right + 1] # 1 indexed
        return []


if __name__ == '__main__':
    s = Solution()

    tests = [
        {"arr": [1,2,3,4], "target": 3},
        {"arr": [-10,-5,0,3,7], "target": -2},
    ]
    for e in tests:
        r = s.twoSum(e['arr'], e['target'])
        print(r)