N = int(input())
A = list(map(int, input()))
result = 0
for i in range(N):
    if i <= len(A):
        result += A[i]
    else:
        break

print(result)