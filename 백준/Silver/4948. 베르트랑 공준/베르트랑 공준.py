import sys
import math
input = sys.stdin.readline
limited = 123456
# 에라토스테네스의 체로 풀기
arr = [1] * ((2 * limited) + 1) # 한정된 숫자까지 1로 가득찬 배열을 만든다.
arr[0] = 0 # 0과 1은 소수가 아니므로 제외
arr[1] = 0
for i in range(2, int(math.sqrt(len(arr)))): # 2부터 n의 제곱근까지 모든 수를 확인
    if arr[i]: # 만약 arr[i]
        for j in range(i + i, len(arr), i): # 2를 제외한 2의 배수, 3을 제외한 3의 배수 등등을 모두 제거한다.
            arr[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(sum(arr[n + 1: (2 * n) + 1]))