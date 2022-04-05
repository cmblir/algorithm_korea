def number(n):
    result = 1 # 결과값
    if n >= 2: # 피보나치는 N = N-2 + N-1이므로 2보다 큰 경우에만 해당된다.
        result = number(n-2) + number(n-1) # 결과값에 해당 공식으로 계산한 값 넣기
    elif n < 2: # 예외처리
        result = n
    return result # 출력

n = int(input())
print(number(n))