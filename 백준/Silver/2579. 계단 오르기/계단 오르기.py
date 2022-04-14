# for문으로 푼 경우
N = int(input())
s = [0 for i in range(301)] # 점수 리스트 / 계단의 개수 300개로 제한
dp = [0 for i in range(301)] # 계단 리스트 / 계단의 개수 300개로 제한 
for i in range(N):
    s[i] = int(input()) # 점수 리스트에 값 넣기
dp[0] = s[0] # 계단이 1개인 경우
dp[1] = s[0] + s[1] # 계단이 2개인 경우
dp[2] = max(s[1] + s[2], s[0] + s[2]) # 계단이 3개인 경우
for i in range(3, N): # 3이상부터
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
    # 계단 리스트는 max()함수를 통해 더 큰 값을 가져온다.
    # dp[0] + s[2] + s[1]
    # dp[-1] + s[3]

print(dp[N - 1])
