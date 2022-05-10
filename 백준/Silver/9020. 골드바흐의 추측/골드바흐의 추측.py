import sys
input = sys.stdin.readline
T = int(input())
# 에라토스테네스의 체 소수 판별 알고리즘 사용
arr = [1] * 10002
arr[0] = 0
arr[1] = 0
for i in range(2, 101): # 2부터 10000은 100의 제곱이므로 100
    if arr[i]:
        for j in range(i + i, 10001, i): # 이전에서 사용한 2의 배수, 3의 배수 등등 소수인 본인을 제외한 모든 배수는 0
            arr[j] = 0

for _ in range(T):
    n = int(input())
    # 이진 탐색 알고리즘 사용
    rf_m = n // 2 # 중간값이면서 좌측값
    lf_m = rf_m # 중간값이면서 우측값
    for _ in range(10000):
        if arr[rf_m] and arr[lf_m]: # 예를 들어 8의 답을 골드바흐 값을 찾을 경우
            # 좌우측 값을 점점 좁혀가면서 rf_m과 rf_m 모두 소수일 경우를 구한다.
            print(rf_m, lf_m)
            break
        rf_m -= 1 # 우측값 1씩 감소
        lf_m += 1 # 좌측값 1씩 증가
