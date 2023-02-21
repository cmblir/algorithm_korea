def solution(my_str, n):
    stack = []
    tmp = 0
    for idx in range(n, len(my_str), n):
        stack.append(my_str[tmp:idx])
        tmp += n
    stack.append(my_str[tmp:])
    return stack