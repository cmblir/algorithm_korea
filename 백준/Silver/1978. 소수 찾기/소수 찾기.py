import sys
T = int(sys.stdin.readline())
N = list(map(int, input().split()))
N_T = [i for i in N if len(N) <= T] # 입력받은 값을 테스트 T 값 범위 안까지만 받는다.
total = 0 # 소수 결과값
for j in N_T: # 입력받은 숫자중
    result = 0 # 소수 판별 소수면 0, 아니면 1
    if j > 1: # 1은 제외하고
        for h in range(2, j): # 2부터 받은 값 전까지 (range(j)는 j-1까지니까)
            if j % h == 0: # 나누어진다면
                result = 1 # 소수가 아니다.
        if result == 0: # 위의 값을 모두 나누었을 때 만약 없다면
            total += 1 # 소수라고 판단하고 결과 +1
print(total)