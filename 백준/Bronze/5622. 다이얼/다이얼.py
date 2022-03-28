num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = list(input()) # 다이얼 입력 값 받기

cnt = 0 # 숫자 세기

for i in alpha: # 입력한 다이얼을 하나씩 쪼개기
    for j in num: # 알파벳 쪼개기
        if i in j: # 만약 입력한 다이얼이 알파벳 안에 있다면
            cnt += num.index(j) + 3 # index갑에서 3을 더해준다.

print(cnt)