import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())
lst = [A, B, C, D, E]
for i in range(len(lst)):
    if lst[i] <= 40:
        lst[i] = 40
print(sum(lst) // 5)