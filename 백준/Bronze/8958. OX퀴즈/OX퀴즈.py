import sys


A = int(sys.stdin.readline())
for i in range(A):
    B = list((sys.stdin.readline()))
    score = 0
    cnt = 1
    for i in B:
        if i == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)