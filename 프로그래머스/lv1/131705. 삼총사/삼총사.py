from itertools import combinations
def solution(number):
    answer = 0
    lst = combinations(number, 3)
    for idx in list(lst):
        if sum(idx) == 0: answer += 1
    return answer