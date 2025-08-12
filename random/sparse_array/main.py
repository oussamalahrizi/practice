#!/usr/bin/env python3

def matchingStrings(stringList : list[str], queries):
    
    seen = []
    for e in queries:
        seen.append([e, 0])
    for e in seen:
        while e[0] in stringList:
            e[1] += 1
            stringList.remove(e[0])
    res = []
    for e in seen:
        res.append(e[1])
    return res


if __name__ == "__main__":
    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    print("\n".join(map(str, res)))
    