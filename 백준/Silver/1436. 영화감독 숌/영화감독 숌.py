import sys
input = sys.stdin.readline
N = int(input())
movie = 666 # 처음 시작하는 숫자 = 숌이 영화를 만들기 시작한 시점
# 브루트 포스로 해당 문제 해결
while N != 0:
    if '666' in str(movie): # 만약 666이라는 문자열이 값에 포함된 경우
        N -= 1 # 찾고자하는 영화까지 1씩 가까워진다.
        if N == 0: # 만약 내가 찾으려는 영화를 찾은 경우
            break
    movie += 1 # 영화의 이름에 +1 씩 계속 더해준다.
print(movie)