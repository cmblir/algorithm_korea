import math
def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        if i != 1: tmp = 1
        else: tmp = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0 and i // j <= 10000000:
                tmp = i // j
                break
        answer.append(tmp)
    return answer