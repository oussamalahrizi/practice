#!/usr/bin/env python3

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        index = 0
        while index < len(s2):
            if s2[index] in s1:
                tmp = list(s1)
                j = index
                while j < len(s2) and s2[j] in tmp:
                    tmp.remove(s2[j])
                    j += 1
                if len(tmp) == 0:
                    return True
            index += 1
        return False


if __name__ == '__main__':
    tests = [
        ["hello", "ooolleoooleh"],
        # ["abc", "lecaabee"],
    ]
    s = Solution()
    for e in tests:
        res = s.checkInclusion(e[0], e[1])
        print(res)
