#!/usr/bin/env python3 


class TimeMap:

    def __init__(self):
        self.timemap = {}

    def get_index(self, arr, value):
        l , r = 0, len(arr) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if arr[mid]['time'] == value:
                return mid
            if arr[mid]['time'] <= value:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timemap.get(key) is None:
            self.timemap[key] = [{'time' : timestamp, 'value' : value}]
            return
        self.timemap.get(key).append({
            'time' : timestamp,
            'value' : value
        })
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemap.get(key)
        if arr is None:
            return None
        index = self.get_index(arr, timestamp)
        return arr[index]['value']
        



if __name__ == '__main__':
    tests = [

    ]
    

    for e in test