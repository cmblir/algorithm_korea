import sys

C = int(sys.stdin.readline())
for i in range(C):
    B = list(map(int, input().split()))
    avg = sum(B[1:]) / B[0]
    result = 0
    for j in B[1:]:
        if avg < j:
            result += 1
    result_avg = ((result / B[0]) * 100)
    print(format(result_avg, ".3f")+"%")