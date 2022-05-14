import sys
T = int(sys.stdin.readline())
for _ in range(T):
    r, e, c = map(int, sys.stdin.readline().split())
    if e - c > r:
        print("advertise")
    elif e - c == r:
        print("does not matter")
    elif e - c < r:
        print("do not advertise")