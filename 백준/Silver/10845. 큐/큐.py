import sys
input = sys.stdin.readline
que = []
T = int(input())
for i in range(T): # 큐 구현
    command = input().split()

    if command[0] == "push": que.insert(0, command[1]) # 큐에 넣는다.
    elif command[0] == "pop": 
        if len(que) != 0: print(que.pop()) # 만약 정수가 있는 경우 뺀값 출력
        else: print(-1) # 없다면 -1 출력
    elif command[0] == "size": print(len(que)) # 큐에 들어있는 정수 개수 출력
    elif command[0] == "empty": # 큐가 비어있다면
        if len(que) == 0: print(1) # 1을 출력
        else: print(0) # 아니라면 0을 출력
    elif command[0] == "front":
        if len(que) == 0: print("-1") # 큐가 비어있다면 -1을 출력
        else: print(que[len(que) - 1]) # 아니라면 가장 앞 정수 출력
    elif command[0] == "back": 
        if len(que) == 0: print("-1") # 큐가 비어있다면 -1을 출력
        else: print(que[0]) # 아니라면 가장 뒤 정수 출력