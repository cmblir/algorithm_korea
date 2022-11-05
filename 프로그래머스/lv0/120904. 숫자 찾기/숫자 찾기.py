def solution(num, k):
    cnt = 1
    for i in str(num):
        if int(i) == k:
            return cnt
        else:
            cnt += 1
    return -1