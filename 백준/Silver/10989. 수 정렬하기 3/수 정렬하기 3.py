def count_sort(num):
    for i in range(10001):
        if num[i] != 0:
            for _ in range(num[i]):
                print(i)


import sys

N = int(input())
num = [0] * 10001
for _ in range(N):
    M = int(sys.stdin.readline())
    
    num[M] = num[M] + 1

count_sort(num)