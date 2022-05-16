import sys
import math
x1, y1, r1 = map(int, sys.stdin.readline().split())
x2, y2, r2 = map(int, sys.stdin.readline().split())
# 기하학으로 접근
D = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# D는 두 과녁 사이의 x축의 차의 제곱과 y축의 차의 제곱의 제곱근을 구한다.
if math.sqrt((r1 + r2) ** 2) > D: print("YES")
# 이때 두 과녁 사이의 반지름의 합이 두 과녁 사이의 거리보다 크다면 
# == 과녁의 크기안에 들어옴
else: print("NO")
# 아니라면