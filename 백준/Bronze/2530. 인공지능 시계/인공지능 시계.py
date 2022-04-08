def count():
    A,B,C = map(int, input().split())
    s = int(input())
    C = C+s # 입력한 초 + 기존 시간 초
    B = B + (C // 60) # 초를 분으로 변환
    C = C%60 # 분을 변환한 만큼 초를 나누기한 몫으로 받기
    A = A + (B // 60) # 분을 시간으로 변환
    B = B%60 # 시간을 변환한 만큼 분을 나누기한 몫으로 받기
    A = A%24 # 시간이 24시간을 넘었을 때 0 이후로 반환하기
    return print(A, B, C)

count()