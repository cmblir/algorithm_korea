import sys
input = sys.stdin.readline
T = int(input())
# 스택으로 해결
answer = []
stack = []
first = 1
cnt = 0
for k in range(T):
    h = int(input())
    while first <= h: # 해당 숫자가 될 때까지 오름차순으로 스택에 쌓는다. 
        # 예를 들어 숫자가 쌓인 first값이 9인데 h가 7이라면
        # 해당 반복문은 무시한다.
        stack.append(first) # first 값은 반복문이 지날동안 1씩 올라가면서
        # 목표한 값까지 넣는다.
        answer.append("+")
        first += 1
    
    # h < first인 경우에 밑에 if문으로 넘어간다.
    if stack[-1] == h: # 내가 빼고자 하는 값이 스택에 있는 경우
        # 예를 들어 4까지 스택에 있는데 3을 빼야한다면
        # 4와 3을 뽑는다.
        stack.pop()
        answer.append("-")
    else: # 수열이 성립하지 않을경우
        print("NO")
        cnt += 1
        break

if cnt == 0: # 수열이 성립하였을 때
    for i in answer:
        print(i)