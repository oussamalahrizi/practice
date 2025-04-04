#!/usr/bin/python3

import sys

def maxProfit(prices: list[int]) -> int:
    maxx = 0
    mini = prices[0]
    for i in range(1, len(prices)):
        mini = min(mini, prices[i - 1])
        maxx = max(maxx, prices[i] - mini)
    
    return maxx if maxx > 0 else 0
        

"""
    [10, 1, 5, 6, 7, 1]
    max : 6
"""

if __name__ == "__main__":
    arr = sys.argv[1].split(' ')
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    print("max profit : ", maxProfit(arr))