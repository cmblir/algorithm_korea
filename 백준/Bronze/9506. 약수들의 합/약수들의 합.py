import sys
while True:
    N = int(sys.stdin.readline())
    if str(N) == "-1":
        break
    tmp = []
    for i in range(1, N):
        if N % i == 0:
            tmp.append(i)
    if sum(tmp) == N:
        print(str(N), end = " ")
        print("=", end = " ")
        for i in range(len(tmp)-1):
            print(str(tmp[i]), end = " + ")
        print(tmp[-1])
    else:
        print(f"{str(N)} is NOT perfect.")