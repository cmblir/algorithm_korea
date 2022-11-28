def solution(my_string):
    stack = []
    for i in my_string:
        if i not in stack: stack.append(i)
        else: pass
    return "".join(stack)