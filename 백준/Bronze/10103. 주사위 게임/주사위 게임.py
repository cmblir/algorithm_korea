import sys
T = int(sys.stdin.readline())
chang = 100
sang = 100
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        sang -= A
    elif A < B:
        chang -= B
print(chang)
print(sang)
