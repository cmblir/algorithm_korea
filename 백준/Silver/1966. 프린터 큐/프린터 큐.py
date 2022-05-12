import sys
input = sys.stdin.readline
K = int(input()) # 테스트 케이스 
# 큐로 해결
for _ in range(K):
    N, M = map(int, input().split()) # 문서의 개수 N, 궁금한 문서가 현재 어디에 놓여있는지 나타내는 M
    printlst = list(map(int, input().split())) # 프린트할 문서 리스트
    check = [0 for _ in range(N)] # DP로 접근
    check[M] = 1 # 궁금한 문서위치 저장
    cnt = 0 # 

    while True:
        if printlst[0] == max(printlst): # 만약 첫번째 값이 가장 큰 값이라면
            cnt += 1

            if check[0] != 1: # 궁금한 문서 위치의 첫번째가 1이 아니라면
                del printlst[0] # 하나씩 넘여가면서 확인한다.
                del check[0] # 하나씩 넘여가면서 확인한다.
            else: # 맞다면
                print(cnt) # 찾았다고 생각하고 프린트
                break
        else:
            printlst.append(printlst[0]) # 첫번째 값을 제일 뒤로 다시 넣고
            check.append(check[0])
            del printlst[0] # 첫번째 값을 삭제한다
            del check[0]