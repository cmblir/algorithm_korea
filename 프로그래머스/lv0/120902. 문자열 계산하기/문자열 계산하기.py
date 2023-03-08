def solution(my_string):
    n = my_string.split()
    result = 0
    for num, idx in enumerate(n):
        if num == 0: result = int(idx)
        if n[num-1] == "+": result += int(idx)
        elif n[num-1] == "-": result -= int(idx)
    return result