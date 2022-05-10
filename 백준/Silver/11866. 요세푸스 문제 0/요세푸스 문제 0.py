import sys
input = sys.stdin.readline
N, K = map(int, input().split())
circle = [i for i in range(1, N + 1)]
num = 0 # 찾고자하는 값 위치
result = [] # 결과를 담을 리스트
for i in range(N):
    num += (K - 1) # 목표값 - 1 (리스트는 0부터 시작하기때문에)
    if num >= len(circle): # 만약 목표값이 전체 길이보다 크다면 뽑아야하는 리스트문
        num %= len(circle) # 내가 제거할 위치의 사람을 전체 수만큼 나누고 남은 값
    result.append(str(circle[num])) # 내가 제거한 사람을 결과 리스트에 넣는다.
    circle.pop(num) # 내가 뽑은 숫자를 pop해준다.
print("<", ', '.join(result),">", sep="")
