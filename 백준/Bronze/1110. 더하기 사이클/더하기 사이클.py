A = int(input())        # 26
B = A                   # 26
cnt = 0                 # 0

while True:
    a = B // 10         # 2   6   8   4
    b = B % 10          # 6   8   4   2
    c = (a + b) % 10    # 8   4   2   6
    B = (b * 10) + c    # 68 84  42  26

    cnt += 1            # 1   2   3   4
    if (B == A):
        break
print(cnt)              # 4