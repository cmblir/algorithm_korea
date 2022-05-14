import sys
while True:
    A, B = map(int , sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    elif A <= B:
        print("No")
    else:
        print("Yes")