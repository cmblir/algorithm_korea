def solution(a, lost, reverse):
    s = set(lost) & set(reverse) # 겹치는 대상 찾기
    l = set(lost) - s # 필요한 학생에서 겹치는 대상 제외
    r = set(reverse) - s # 가지고 있는 학생에서 겹치는 대상 제외
    for i in sorted(r):
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)
    return a - len(l)
