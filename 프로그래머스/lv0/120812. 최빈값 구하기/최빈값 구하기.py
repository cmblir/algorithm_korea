def solution(array):
    dd = {}
    for idx in array:
        if str(idx) not in dd.keys(): dd[str(idx)] = 1
        else: dd[str(idx)] += 1
    result = []
    max_v = max(dd.values())
    for k, v in dd.items():
        if v == max_v: result.append(k)
    if len(result) != 1: return -1
    else: return int(result[0])