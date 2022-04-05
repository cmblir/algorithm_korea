def factory(N): # 팩토리 정의
    result = 1 # 기본값 1로 정의
    if N > 0: # 넣는 값이 0 이상일 경우
        result = N * factory(N-1) # 결과값은 입력값 * 이전 주소값
    return result # 결과값 리턴

N = int(input())
print(factory(N))