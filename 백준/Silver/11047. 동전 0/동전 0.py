import sys
N, K = map(int, sys.stdin.readline().split())
value = []
for _ in range(N):
    A = int(sys.stdin.readline())
    value.append(A)
value.sort(reverse= True)
result = 0
for i in value:
    if K <= 0:
        break
    elif K > 0:
        result += K // i
        K -= i * (K // i)
print(result)