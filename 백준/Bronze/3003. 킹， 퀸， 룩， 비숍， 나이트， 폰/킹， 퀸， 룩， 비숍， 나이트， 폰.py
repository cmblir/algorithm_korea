A = list(map(int, input().split()))
result = [1, 1, 2, 2, 2, 8] # 원래 있어야하는 말의 개수
for i in range(len(result)):
    print(result[i] - A[i], end = ' ') # 원래 있어야할 말의 개수 - 현재 가지고 있는 말의 개수, 끝은 띄어쓰기로