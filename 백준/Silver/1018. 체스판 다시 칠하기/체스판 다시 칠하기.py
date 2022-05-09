import sys
n, m = map(int, sys.stdin.readline().split())
writed = []
count = []
for i in range(n):
    writed.append(str(input()))
for i in range(n-7): # 8X8 크기의 체스판을 자르는 것
    for j in range(m-7): # 8X8 크기의 체스판을 자르는 것
        black_paint = 0
        white_paint = 0
        for a in range(i,i+8): # 8X8 크기의 체스판을 자르는 것
            for b in range(j,j+8): # 8X8 크기의 체스판을 자르는 것
                if (a+b)%2==0:
                    if writed[a][b]!='W': # 화이트보드가 비어있지않다면
                        black_paint +=1
                    if writed[a][b]!='B': # 화이트보드가 비어있다면
                        white_paint +=1
                else:
                    if writed[a][b]!='B': # 화이트보드가 비어있지않다면
                        black_paint +=1
                    if writed[a][b]!='W': # 화이트보드가 비어있다면
                        white_paint +=1
        count.append(min(black_paint,white_paint))

print(min(count))