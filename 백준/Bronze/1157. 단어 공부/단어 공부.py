A = list(input().lower()) # 받은 값을 모두 소문자로
B = list(set(A)) # 중복값 제거
tmp = [] # 각 문자열 카운트해서 넣을 리스트
for i in B: # 중복값이 제거된 문자열의 문자들
    tmp.append(A.count(i)) # 받은 값에서 중복값을 제거한 문자 카운트세서 리스트에 넣기

if tmp.count(max(tmp)) > 1: # 리스트에서 가장 큰 값 개수가 1보다 많은 경우
    print("?")
else:
    max_index = tmp.index(max(tmp)) # 리스트에서 가장 큰 값이 있는 리스트의 문자를 정의
    print(B[max_index].upper()) # 중복값이 제거된 리스트에서 가장 큰 값을 가진 문자를 대문자로 출력
