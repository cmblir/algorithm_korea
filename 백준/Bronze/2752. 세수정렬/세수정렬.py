A = list(map(int, input().split()))
def num(A):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

print(*num(A))