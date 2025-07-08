#!/usr/bin/env python3


def isPalindrome(s: str) -> bool:
        left  = 0
        right = len(s) - 1
        while left < right:
            while left < right and not isalnum(s[left]):
                 left += 1
            while left < right and not isalnum(s[right]):
                 right -= 1   
            if s[left].lower() != s[right].lower():
                 return False
            left += 1
            right -= 1
        return True

def isalnum(c):
     return ord('a') <= ord(c) <= ord('z') or \
     ord('0') <= ord(c) <= ord('9') or \
     ord('A') <= ord(c) <= ord('Z')

if __name__ == '__main__':
    tests = [
         "Was it a car or a cat I saw?",
         "tab a cat"
    ]
    for e in tests:
         r = isPalindrome(e)
         print(r)