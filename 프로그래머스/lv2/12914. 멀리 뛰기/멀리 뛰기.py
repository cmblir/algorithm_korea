def solution(n):
    if n > 3:
        tmp = [0] * (n + 1)
        tmp[1] = 1
        tmp[2] = 2
        for i in range(3, n + 1):
            tmp[i] = tmp[i - 1] + tmp[i - 2]
        return tmp[n] % 1234567
    else:
        return n