N = str(input()) # 입력값

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 문자

for i in cro: # 크로아티아 문자 내에 있으면
    N = N.replace(i, '*') # 만약 N에 크로아티아 문자가 있으면 N문자에 덮붙여서 문제 해결한다.

print(len(N))
