import sys
T = int(sys.stdin.readline())
AB = str(input())
if AB.count("A") > AB.count("B"):
    print("A")
elif AB.count("B") > AB.count("A"):
    print("B")
else:
    print("Tie")