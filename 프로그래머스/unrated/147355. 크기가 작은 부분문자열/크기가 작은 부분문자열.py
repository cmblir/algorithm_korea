def solution(t, p):
    temp = []
    for idx in range(len(t)-len(p)+1): temp.append(t[idx:idx+len(p)])
    answer = [i for i in temp if int(i) <= int(p)]
    print(answer)
    return len(answer)