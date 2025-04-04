#!/usr/bin/python3


import sys

"""
    1, 2
    "ab"
    "aab"
"""


def lengthOfLongestSubstring(s: str) -> int:
    maxx = 0
    string = ""
    i = 0
    while i < len(s):
        
        if string.find(s[i]) == -1:
            string += s[i]
        else:
            maxx = max(maxx, len(string))
            string = string[1:]
            i -= 1
        i += 1
    return max(maxx, len(string))

if __name__ == "__main__":
    arr = sys.argv[1]

    print("solution : ", lengthOfLongestSubstring(arr))