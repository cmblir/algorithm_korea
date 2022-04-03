import sys
T = int(sys.stdin.readline())
N = list(map(int, input().split()))
N_T = [i for i in N if len(N) <= T]
total = 0
for j in N_T:
    result = 0
    if j > 1:
        for h in range(2, j):
            if j % h == 0:
                result = 1
        if result == 0:
            total += 1
print(total)