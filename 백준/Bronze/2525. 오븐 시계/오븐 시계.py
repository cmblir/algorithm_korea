A, B = map(int, input().split())
C = int(input())

A += C // 60   # 추가되는 분에 대해서 60으로 나눈 값
B += C % 60    # 추가되는 분에 대해서 60으로 나누고 남은 값

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A, B)
    