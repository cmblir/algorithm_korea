def solution(x, y):
    before = {}
    after = {}
    for idx in range(len(x)):
        if x[idx] not in before: before[x[idx]] = 1
        else: before[x[idx]] +=1
        if y[idx] not in after: after[y[idx]] = 1
        else: after[y[idx]] += 1
    return 1 if before == after else 0