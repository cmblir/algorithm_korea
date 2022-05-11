import sys
input = sys.stdin.readline
stack = []
T = int(input())
for i in range(T): # 스택 구현
    command = input().split()
    if command[0] == "push": stack.append(command[1]) # 스택에 쌓는다.
    elif command[0] == "pop": 
        if len(stack) != 0: print(stack.pop()) # 만약 정수가 있는 경우 뺀값 출력
        else: print(-1) # 없다면 -1 출력
    elif command[0] == "size": print(len(stack)) # 스택에 들어있는 정수 개수 출력
    elif command[0] == "empty": # 스택가 비어있다면
        if len(stack) == 0: print(1) # 1을 출력
        else: print(0) # 아니라면 0을 출력
    elif command[0] == "top": # 스택의 가장 위에 있는 정수 출력
        if len(stack) == 0: print("-1")
        else: print(stack[-1])