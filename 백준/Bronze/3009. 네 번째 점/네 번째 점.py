li_x = []
li_y = []
for i in range(3): # 4번째 점을 구하는 것이기때문에 3번째 점까지만 받는다.
    x, y = map(int, input().split())
    li_x.append(x) # 받은 x값 넣기
    li_y.append(y) # 받은 y값 넣기
for j in range(3): # 다시 반복문을 통해 x와 y에 해당 값이 있는 지 확인
    if li_x.count(li_x[j]) == 1: # 만약 x의 j위치에 값이 1개밖에 없다면
        x = li_x[j] # x 는 받은 x의 j위치 값이다.
    if li_y.count(li_y[j]) == 1: # 만약 y의 j위치에 값이 1개밖에 없다면
        y = li_y[j] # y 는 받은 y의 j위치 값이다.
print(x, y)