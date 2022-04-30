N, M = map(int, input().split())
H = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i + 1, N):
        for h in range(j + 1, N):
            if (H[i] + H[j] + H[h]) > M:
                continue
            else:
                result = max(result, H[i] + H[j] + H[h])
print(result)