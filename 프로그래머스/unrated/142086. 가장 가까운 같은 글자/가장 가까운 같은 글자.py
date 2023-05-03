def solution(s):
    result = []
    cnt = {}
    for num, idx in enumerate(s):
        if idx not in cnt:
            cnt[idx] = num
            result.append(-1)
        else:
            result.append(num - cnt[idx])
            cnt[idx] = num
    return result