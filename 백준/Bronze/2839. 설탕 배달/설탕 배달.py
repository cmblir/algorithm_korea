N = int(input()) # 설탕 킬로그램수

bag = 0
while N >= 0: # N값이 0보다 크다면
    if N % 5 == 0: # N을 5로 나눴을 때 0이 나오면
        bag += N // 5 # N으로 나눈 값을 넣은다.
        print(bag)
        break
    N -= 3 # 5로 나눈 나머지값들은 5개 될때까지 3을 빼주고
    bag += 1 # bag에 3을 뺀만큼 +1씩 더해준다.
else:
    print(-1)
