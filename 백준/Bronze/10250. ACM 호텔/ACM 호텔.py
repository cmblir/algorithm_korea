T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    # H는 층수, W는 방 개수, N은 N번째 손님
    cnt = 1
    while (N - (cnt * H)) > 0:
        cnt += 1
    height = N - ((cnt - 1) * H)
    if cnt < 10:
        print(f"{height}0{cnt}")
    else:
        print(f'{height}{cnt}')