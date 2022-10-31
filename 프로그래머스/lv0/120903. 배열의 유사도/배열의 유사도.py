def solution(s1, s2):
    answer = 0
    for i in max(s1, s2):
        if i in min(s1, s2):
            answer += 1
    return answer