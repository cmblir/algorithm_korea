import sys
input = sys.stdin.readline
N = str(int(input()))
cnt = 0
for i in N:
    cnt += int(i) ** 5
print(cnt)