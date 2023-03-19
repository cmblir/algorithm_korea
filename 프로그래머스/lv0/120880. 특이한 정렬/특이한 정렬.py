def solution(numlist, n):
    dicts = {}
    result = []
    between = []
    for idx in numlist: dicts[idx] = abs(n - idx)
    st = sorted(dicts.items(), key=lambda x: x[1])
    for idx in range(len(st)-1):
        if st[idx][1] == st[idx+1][1]:
            between.append(st[idx][0])
            between.append(st[idx+1][0])
        else:
            if len(between) > 1:
                between.sort(reverse = True)
                for i in between:
                    result.append(i)
                between = []
            else:
                result.append(st[idx][0])
    result.append(st[-1][0])
    return result