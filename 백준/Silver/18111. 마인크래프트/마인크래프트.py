from math import inf
import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)] # 현재 블록
h = 0 # 현재 높이
answer = inf # 시간초과방지를 위한 큰수
for i in range(257): # 현재 높이 ~ 최대 블록수
    min = 0 # 쌓을 블록
    max = 0 # 뺄 블록
    for j in range(N): # 현재 블록의 높이
        for k in range(M): # 현재 블록의 길이
            if blocks[j][k] < i:
                min += (i - blocks[j][k])
            # 만약 해당 블록이 현재 높이보다 낮다면
            # 인벤토리에서 현재 높이만큼 붙인다.
            else:
                max += (blocks[j][k] - i)
            # 아니라면 현재 높이만큼 뺀다
    inven = max + B # 뺀만큼의 블럭 + 인벤토리
    if inven < min: # 만약 뺀 블록을 더했을 때 내가 붙인 블록보다 작다면
        continue
    time = 2 * max + min # 지난 시간은 뺀 블럭 * 2 + 쌓은 블록
    if time <= answer: # 만약 인벤토리 최대크기보다 사용한 시간이 작거나 같다면
        answer = time # 현재 걸린 시간이 정답이 된다.
        h = i # 높이는 현재 위치
print(answer, h)
