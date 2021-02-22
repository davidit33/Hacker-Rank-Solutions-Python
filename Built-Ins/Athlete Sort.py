#!/bin/python3
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append([int(i) for i in input().split(' ')])
k = int(input())
arr = sorted(list(arr), key = lambda x: x[k])
for i in arr:
    print(*i)





