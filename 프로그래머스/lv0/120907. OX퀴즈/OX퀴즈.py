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