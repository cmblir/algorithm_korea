def solution(N):
    for i in range(1, S+1):
        if (i + 1) * (i / 2) > N:
            return i - 1
        elif (i + 1) * (i / 2) == N:
            return i
S = int(input())
print(solution(S))