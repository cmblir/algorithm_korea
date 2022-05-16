import sys
input = sys.stdin.readline
cnt = 0
while True:
    N = int(input())
    if N == -1: break
    else: cnt += N
print(cnt)