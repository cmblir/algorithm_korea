L, P = map(int, input().split()) # 사람 수 L, 파티 넓이 P
N = list(map(int, input().split())) # 각 기사에 실려있는 참가자 수
result = []
for i in N: # 각각의 기사에 대한 참가자 수
    result.append(str(i - (L * P))) # 기사에 나온 참가자 수 - 파티 참가자 수
print(' '.join(result))