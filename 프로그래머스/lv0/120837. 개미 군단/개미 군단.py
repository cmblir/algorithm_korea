import math
def solution(hp):
    result = 0
    result += math.floor(hp / 5)
    hp %= 5
    result += math.floor(hp / 3)
    hp %= 3
    result += math.floor(hp / 1)
    return result