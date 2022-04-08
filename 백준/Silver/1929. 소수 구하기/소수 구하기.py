def get_prime(N, M): # 에라토스테네스의 체
    sieve = [False,False] + [True for i in range(2, M+1)]
    # 0과 1은 소수가 아니므로 False를 넣고, 2부터 M까지 True값을 넣은 리스트 생성
    m = int(M ** 0.5) # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    for x in range(2, m + 1): # 2부터 최대약수 m까지 반복
        if sieve[x] == True: # i가 소수인 경우
            for y in range(x+x, M + 1, x): # i 이후 i의 배수들을 False 판정
                sieve[y] = False
    
    return [x for x in range(N, M+1) if sieve[x] == True]
    # 반복문을 다 돌고나서 sieve[x] 값이 True인 경우는 소수인 경우에 속한다.

N, M = map(int, input().split())
result = get_prime(N, M)

if len(result) != 0: # 결과값 길이가 0이 아니라면
    for i in result:
        print(i)