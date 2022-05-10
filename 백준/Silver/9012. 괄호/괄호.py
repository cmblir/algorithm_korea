import sys
input = sys.stdin.readline
N = int(input())
PS = []
for i in range(N):
    PS.append(str(input())[:-1])
for i in PS:
    cnt = 0
    if i[-1] == "(" or i[0] == ")" or len(i) % 2 != 0:
        print("NO")
    else:
        for j in range(len(i)):
            if cnt < 0:
                break
            if i[j] == "(":
                cnt += 1
            else:
                cnt -= 1
        print("YES") if cnt == 0 else print("NO")