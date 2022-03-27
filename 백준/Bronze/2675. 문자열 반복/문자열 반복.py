T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    H = []
    for j in S:
        H.append(j * int(R))
    P = "".join(H)
    print(P)