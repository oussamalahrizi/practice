#!/usr/bin/python3

import sys

def max_books(books : list):
    max = 0
    i = 0
    prev = 0
    temp = []
    max_final = []
    while i < len(books):
        if len(temp) < 5:
            max += books[i]
            temp.append(books[i])
            max_final = temp
            prev = max
        else:
            prev -= temp.pop(0)
            temp.append(books[i])
            prev += books[i]
            if prev > max:
                max = prev
                max_final = temp.copy()
        i += 1

    print("max 5 books : ", max_final, "max value : ", max)

if __name__ == "__main__":
    books = sys.argv[1].split()
    final = []
    for b in books:
        final.append(int(b))
    max_books(final)

