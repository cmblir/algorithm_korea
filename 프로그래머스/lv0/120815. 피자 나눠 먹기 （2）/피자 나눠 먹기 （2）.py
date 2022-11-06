def solution(x):
    for i in range(max(6, x), (6*x)+1):
        if i % 6 == 0 and i%x ==0:
            return i // 6