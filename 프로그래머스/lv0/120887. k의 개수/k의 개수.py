def solution(i, j, k):
    result = 0
    for idx in range(i, j+1): result += str(idx).count(str(k))
    return result