def solution(s):
    n = s.split()
    result = 0
    for num, idx in enumerate(n):
        if idx != "Z": result += int(idx)
        elif idx == "Z": result -= int(n[num-1])
    return result