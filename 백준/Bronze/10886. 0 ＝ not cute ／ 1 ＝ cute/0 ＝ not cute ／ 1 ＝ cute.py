import sys
T = int(sys.stdin.readline())
result = []
for _ in range(T):
    result.append(str(input()))
if result.count("0") > result.count("1"):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
