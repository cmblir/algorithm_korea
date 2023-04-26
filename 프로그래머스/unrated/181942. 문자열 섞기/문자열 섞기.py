def solution(str1, str2):
    answer = []
    for idx, jdx in zip(str1, str2):
        answer.append(idx)
        answer.append(jdx)
    return "".join(answer)