import sys
T = int(sys.stdin.readline())
for _ in range(T):
    soju = {}
    N = int(sys.stdin.readline())
    for _ in range(N):
        S, L = list(map(str, input().split()))
        soju[S] = int(L)
    print(max(soju, key=soju.get))