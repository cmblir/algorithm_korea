import math
A = list(map(int, input().split()))
result = 0
for i in A:
    c = math.pow(i, 2)
    result += c
print(math.floor(result % 10))
