T = int(input()) # 테스트 케이스 T
for i in range(T):
    k = int(input()) # a층
    n = int(input()) # b호
    floor = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]
    
    print(floor[-1])