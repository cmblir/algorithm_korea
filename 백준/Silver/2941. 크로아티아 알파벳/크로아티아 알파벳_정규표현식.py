import re # 정규표현식
N = str(input()) # 입력값
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 문자

for i in cro: # 크로아티아 리스트 내의 문자열
    if re.search(i, N): # i값이 N에 있으면
        N = N.replace(i, '*') # 크로아티아 문자열이 있으면 대체를 한다.



print(len(N))
