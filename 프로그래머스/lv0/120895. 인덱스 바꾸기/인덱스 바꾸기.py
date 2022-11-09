def solution(x, y, z):
    x = [i for i in x]
    x[y], x[z] = x[z], x[y]
    return "".join(x)