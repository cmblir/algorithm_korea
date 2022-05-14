import sys
input = sys.stdin.readline
T = int(input())
result = []
for i in range(T):
    H = list(map(int, input().split()))
    if H[0] == H[1] == H[2]:
        result.append(10000 + H[1] * 1000)
    elif H[0] == H[1] or H[1] == H[2]:
        result.append(1000 + H[1] * 100)
    elif H[0] == H[2]:
        result.append(1000 + H[0] * 100)
    else:
        result.append(max(H) * 100)
print(max(result))