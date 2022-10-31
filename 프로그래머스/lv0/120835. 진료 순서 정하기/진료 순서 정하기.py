def solution(emergency):
    tmp = sorted(emergency, reverse = True)
    result = [tmp.index(i) + 1 for i in emergency]
    return result