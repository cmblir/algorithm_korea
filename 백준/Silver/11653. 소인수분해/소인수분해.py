N = int(input())
def num(N):
    result = [] # 결과값
    dev = N # 임의의 변수, N값을 저장할 dev
    while dev != 1: # 만약 1이 아니라면(1은 더이상 안나눠지므로)
        for i in range(2, N+1):  # 2~N까지의 숫자로 나누었을때 (소수를 찾기위해서)
            if dev % i == 0: # i값으로 나눠진다면
                dev = dev // i # N값을 저장한 dev는 i로 나눈 값이 된다.
                result.append(i) # 그 값을 리스트에 저장
                break # 나누기를 했다면 while문 break
    return result # dev가 1이 되었을 경우 (더이상 나눠지지않는 수가 되었을 경우 == 소인수 분해 완료)

for i in num(N): # 정답 리스트의 값들을 백준 출력값에 맞게끔 출력
    print(i)