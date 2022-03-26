import sys

A = int(sys.stdin.readline())
B = list(map(int, input().split()))
max = max(B)

num = []
for i in B:
    num.append((i / max) * 100)
result = (sum(num) / A)
print(result)