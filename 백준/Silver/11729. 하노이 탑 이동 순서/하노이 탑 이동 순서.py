n = int(input())
def counter():
    cnt = 1
    def hanoi(n, A=1, B=3, m=2):
        nonlocal cnt
        cnt += 1
        # A는 시작지점, B는 도착지점, m은 중간지점(시작하는 위치에서 도착으로 못갈경우 들리는 지점)
        if n == 1: # N값이 1이라면, (내가 쌓고자하는 원판 수가 1개가 남았을 경우)
            print(A, B)
            return
        hanoi(n -1, A, m, B) # 맨 밑의 원판을 제외하고 원판을 시작지점에서 중간지점으로 옮긴다,
        print(A, B)
        hanoi(n -1, m, B, A) # 맨 밑의 원판을 제외하고 원판을 중간지점에서 도착지점을 옮긴다.
    for i in range(n -1): # 함수가 돌아가는 동안 입력값 - 1의 범위 만큼
        cnt = (cnt * 2) + 1 # 횟수를 카운트해준다. 단 매 카운트 *2 +1을 해준다.
    print(cnt)
    hanoi(n)

counter()