min = 0
sec = 0
for i in range(4):
    A = int(input())
    min += A // 60 # 60초(1분)로 나눠준 만큼 분을 더한다.
    sec += A % 60 # 60초(1분)로 나누고 남은 값을 더한다.
    if sec >= 60: # 만약 초시간이 60초(1분)을 넘어가면
        min += sec // 60 # 초를 60초(1분)으로 나눈만큼 더한다.
        sec -= (60 * (sec // 60)) # 나눈만큼 뺀다.
print(min)
print(sec)