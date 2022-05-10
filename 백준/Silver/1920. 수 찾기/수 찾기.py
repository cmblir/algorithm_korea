import sys
input = sys.stdin.readline
n = int(input())
N = sorted(map(int, input().split())) # 이분탐색을 위한 정렬
m = int(input())
M = map(int, input().split())

def binary(l, N, start, end): # 이분탐색법
    if start > end:
        return 0
    middle = (start + end)// 2 # 중간인덱스
    if l == N[middle]: # 동일한 값을 찾았다!
        return 1 # 리턴 1
    elif l < N[middle]: # 중간값보다 작다
        return binary(l, N, start, middle - 1) # 중간값을 줄여가면서 다시 탐색
    else: # 중간값보다 크다
        return binary(l, N, middle+1, end) # 중간값을 늘려가면서 탐색

for l in M:
    start = 0 # 시작 인덱스
    end = len(N) - 1 # 끝 인덱스
    print(binary(l, N, start, end))