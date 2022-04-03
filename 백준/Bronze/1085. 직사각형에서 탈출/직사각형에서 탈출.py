x, y, w, h = map(int, input().split()) # 지표상의 한수 (x,y) 값과 우측 상단 꼭지점 (w, h)
wide = w - x # 거리는 무조건 +이므로 절대값 구현
height = h - y # 거리는 무조건 +이므로 절대값 구현
x = abs(x) # 거리는 무조건 +이므로 절대값 구현
y = abs(y) # 거리는 무조건 +이므로 절대값 구현
if wide <= height and wide <= x and wide <= y: # 직사각형에서 한수 x의 거리 계산값
    print(wide)
elif height <= wide and height <= x and height <= y: # 직사각형에서 한수 y의 거리 계산값
    print(height)
elif x <= wide and x <= height and x <= y: # 원점으로부터 한수 x의 거리 계산값
    print(x)
elif y <= wide and y <= height and y <= x: # 원점으로부터 한수 y의 거리 계산값
    print(y)