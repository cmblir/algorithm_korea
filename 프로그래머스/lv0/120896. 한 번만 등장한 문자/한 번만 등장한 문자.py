def solution(s):
    stack = []
    for idx in s:
        if s.count(idx) == 1: stack.append(idx)
    return "".join(sorted(stack))