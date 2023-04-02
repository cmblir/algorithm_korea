# 신규 풀이 방식
def solution(quiz):
    result = []
    for idx in quiz:
        idx = idx.replace("=","==")
        if eval(idx): result.append("O")
        else: result.append("X")
    return result

"""
이전 풀이 방식
def solution(quiz):
    result = []
    for idx in quiz:
        tmp = idx.split()
        score = 0
        for jdx in range(len(tmp)):
            if jdx == 0: score = int(tmp[jdx])
            elif tmp[jdx] == "-": score -= int(tmp[jdx+1])
            elif tmp[jdx] == "+": score += int(tmp[jdx+1])
            elif tmp[jdx] == "=":
                if int(score) == int(tmp[jdx+1]): result.append("O")
                else: result.append("X")
    return result
"""