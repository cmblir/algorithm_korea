def solution(A, B):
    cnt = 0
    if A == B: return 0
    tmp = [i for i in A]
    while cnt < 101:
        tmp.insert(0, tmp[-1])
        tmp.pop()
        cnt += 1
        front = "".join(tmp)
        if front == B: return cnt
    return -1