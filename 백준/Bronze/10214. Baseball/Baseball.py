import sys
T = int(sys.stdin.readline())
for _ in range(T):
    win = {"Yonsei": 0,
           "Korea": 0}
    for _ in range(9):
        y, k = map(int, sys.stdin.readline().split())
        win["Yonsei"] += y
        win["Korea"] += k
    if win["Yonsei"] > win["Korea"]:
        print("Yonsei")
    elif win["Yonsei"] < win["Korea"]:
        print("Kore")
    else:
        print("Draw")