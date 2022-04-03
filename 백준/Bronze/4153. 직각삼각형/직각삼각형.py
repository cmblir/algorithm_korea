import math # 제곱 사용을 위해 math 라이브러리 불러오기
while True:
    a, b, c = map(int, input().split())
    if a != 0 and b != 0 and c != 0: # 모든 값이 0 0 0 이 아니라면
        if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2): # 피타고라스 정리 a^2 + b^2 = c^2
            print('right')
        elif math.pow(b, 2) + math.pow(c, 2) == math.pow(a, 2): # 피타고라스 정리 b^2 + c^2 = a^2
            print('right')
        elif math.pow(a, 2) + math.pow(c, 2) == math.pow(b, 2): # 피타고라스 정리 a^2 + c^2 = b^2
            print('right')
        else:
            print('wrong')
    else:
        break
