import sys
n = int(sys.stdin.readline())
visit = []
result = 0
for i in range(n):
    visit.append(str(input()))
    # 대행사를 통해 나미비아 비자를 받는 비용 140
    # 남아프리카공화국에서 비자를 받는 비용 40
    # 케냐 비자 비용 50 = 1회 / 100 = 다회
    # 무비자 입국 가능 국가 = 남아프리카공화국(30일), 보츠와나(90일)
    # 짐바브웨 비자 비용 30 = 1회 / 45 = 2회
    # 잠비아 비자 비용 50 = 1회 / 80 = 2회
    # 위 두 국가 동시 방문 비자 50 / 단, 잠바브웨 또는 잠비야에서 다른데로 가면 비자 소멸
    # 탄자니아 비자 비용 50 = 1회 / 100 = 다회
    # 에티오피아 50
tmp = []
for i in range(len(visit)):
    tmp.append(visit[i])
    if visit[i] == "botswana":
        pass
    elif visit[i] == "ethiopia":
        result += 50
    elif visit[i] == "kenya":
        result += 50
    elif visit[i] == "namibia":
        if "south-africa" in tmp:
            result += 40
        else:
            result += 140
    elif visit[i] == "south-africa":
        pass
    elif visit[i] == "tanzania":
        result += 50
    elif visit[i] == "zambia":
        if "zimbabwe" in tmp[i - 1]:
            result += 20
        else:
            result += 50
    elif visit[i] == "zimbabwe":
        if "zambia" in tmp[i - 1]:
            pass
        else:
            result += 30

print(result)