# 스택으로 해결
while True:
    h = str(input())
    stack_1 = []
    result = 1 # True인지 False인지 확인을 위해 추후 이중조건문
    if h == '.':
        break
    for i in h:
        if i == "[" or i == "(": # 해당 문자열이 괄호를 여는 것이면
            stack_1.append(i) # 스택에 쌓는다.
        elif i == ")": # 만약 소괄호를 닫는 것이라면
            if not stack_1 or stack_1[-1] == '[': # 스택에 없거나, 스택의 마지막 글자가 대괄호 라면
                result = 0
                break # 정답이 아니다
            else:
                stack_1.pop() # 위의 두 조건문이 아니기에 괄호를 삭제한다.
        elif i == "]": 
            if not stack_1 or stack_1[-1] == '(':
                result = 0
                break
            else:
                stack_1.pop()
    if len(stack_1) == 0 and result == 1: # 스택에 남은 괄호가 없고 중간에 break가 안걸린 상태인 경우
        print("yes")
    else:
        print("no")