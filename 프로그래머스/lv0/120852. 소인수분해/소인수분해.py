stack = []
def fact(x):
    d = 2
    while d <= x:
        if x % d == 0:
            stack.append(d)
            x = x / d
        else: d = d + 1
def solution(x):
    fact(x)
    return sorted(list(set(stack)))