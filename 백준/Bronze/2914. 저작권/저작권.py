import math
A, I = map(int, input().split()) # A는 수록곡, I는 평균값
print((A * (I - 1) + 1)) # 평균을 올림했으니까 -1해주고, 나중에 + 1해줘서 구한다.