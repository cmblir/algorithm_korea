import sys
input = sys.stdin.readline
n = int(input())

result = []
for _ in range(n):
    x, y = map(int, input().split())
    result.append([x, y])

result.sort(key = lambda x : (x[0], x[1]))
for i in range(n):
    print(result[i][0], result[i][1])