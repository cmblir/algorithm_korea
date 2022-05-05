import sys
input = sys.stdin.readline
n = int(input())
result  = []
for _ in range(n):
    w, h = map(int, input().split())
    result.append([w, h])

tt = []
for i in range(len(result)):
    tmp = 0 # 등수에서 밀린 횟수 (자기 자신이 있으므로 0등부터)
    for j in range(len(result)):
        if result[i][0] < result[j][0] and result[i][1] < result[j][1]: # 만약 모든거에서 진다면 +1
            tmp += 1
    tt.append(tmp + 1)
print(' '.join(str(x) for x in tt)) # 한 줄에 출력하기