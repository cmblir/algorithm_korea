T = int(input()) # 테스트 케이스 T
for i in range(T):
    k = int(input()) # 층수
    n = int(input()) # 호수
    floor = [i for i in range(1, n+1)] # 전체 층수의 사람들을 하나의 리스트로 만들기

    for i in range(k): # k 층수만큼 반복
        for j in range(1, n): # n 호수 + 1만큼 반복
            floor[j] += floor[j-1] # 기존에 있던 리스트에 호수의 사람들을 계산한 만큼 넣기
    
    print(floor[-1]) # 최종 목표인 (k-1)층의 사람수 세기
