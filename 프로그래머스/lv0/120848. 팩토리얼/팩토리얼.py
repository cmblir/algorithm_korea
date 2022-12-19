def solution(x):
    cnt = 1
    answer = 0
    for i in range(1, x+1):
        if cnt*i <= x:
            cnt *= i
            answer = i
        elif cnt*i > x:
            break
    return answer