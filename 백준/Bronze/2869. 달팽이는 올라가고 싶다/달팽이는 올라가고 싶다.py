import math
A, B, V = map(int, input().split())
# A는 낮에 올라가기, B는 밤에 미끌, V는 목표높이

day = (V - B) / (A - B)
# A - B = 낮에 올라가고 미끄러진 값
print(math.ceil(day))
# 문제 5 1 6의 경우 6 - 1 / 5 - 1 이므로 5/4가 나온다. 이걸 올림하기위해서
# ceil을 써준다. 