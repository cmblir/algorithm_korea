import math
R = int(input())
print(format(round((math.pow(R, 2) * math.pi), 6), ".6f"))
# 유클리드 기하학 원의 넓이 공식 반지름^2 * 원주율
print(format(round((2 * math.pow(R ,2)), 6), ".6f"))
# 택시 기하학 원의 넓이 공식 2 * 반지름^2