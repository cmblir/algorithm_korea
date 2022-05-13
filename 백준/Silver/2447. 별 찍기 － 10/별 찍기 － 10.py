import sys
N = int(sys.stdin.readline())
star = [[0 for _ in range(N)] for _ in range(N)]
 # DP로 접근
def solution(n): # 별을 찍기위한 기본 베이스 만들기
    if n == 3: # N이 3이 되는경우 재귀문을 멈춘다.
        """
        *** star[0][:3]
        * * star[1][:3]
        *** star[2][:3]
        """
        star[0][:3] = star[2][:3] = [1] * 3
        star[1][:3] = [1, 0, 1]
        return
    empty = n // 3 # 정사각형을 크기 N//3 패턴으로 둘러싼 형태
    solution(n//3)
    for i in range(3): # 별 배열을 찍기위한 반복문
        for j in range(3):
            if i == 1 and j == 1:
                continue # 1인 경우는 그냥 넘어간다.
            for k in range(empty):
                star[empty * i + k][empty * j : empty * (j + 1)] = star[k][:empty]
                # n = 3^(i-1) 일때의 별 배열
solution(N)
for i in star:
    for j in i: # 내가 만든 배열안에서
        if j: # j가 1인 경우에는 별찍기
            print("*", end = '')
        else: # 아니라면 빈칸 만들기
            print(" ", end = '')
    print()