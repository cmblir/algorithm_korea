N, T, C, P = map(int, input().split())
cnt = 0
result = 0
for i in range(N):
    cnt += T
    if cnt >= N:
        break
    else:
        result += C
print(P * result)