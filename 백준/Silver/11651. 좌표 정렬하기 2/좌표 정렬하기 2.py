import sys
input = sys.stdin.readline
arr = [] # 문제의 요점인 y좌표가 증가하는 순으로
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y, x]) # y값을 기준으로 정렬되게끔

arr.sort() # y값을 기준으로 좌표가 정렬된다.
for y, x in arr:
    print(x, y)