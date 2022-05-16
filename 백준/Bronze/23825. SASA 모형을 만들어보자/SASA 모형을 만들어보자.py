import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # S모양의 블록, A모양의 블록
lst = [N // 2, M // 2]
print(min(lst))
