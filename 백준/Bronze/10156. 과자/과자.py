# 10156 과자
import sys
input = sys.stdin.readline
K, N, M = map(int, input().split())
buy = K * N
if buy >= M: 
    print(buy - M)
else:
    print(0)