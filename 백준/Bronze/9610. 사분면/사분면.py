import sys
N = int(sys.stdin.readline())
axis = 0
grap = {'Q1': 0,
        'Q2': 0,
        'Q3': 0,
        'Q4': 0}
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 or y == 0:
        axis += 1
    if x > 0 and y > 0:
        grap['Q1'] += 1
    elif x > 0 and y < 0:
        grap['Q4'] += 1
    elif x < 0 and y < 0:
        grap['Q3'] += 1
    elif x < 0 and y > 0:
        grap['Q2'] += 1
print(f"Q1: {grap['Q1']}")
print(f"Q2: {grap['Q2']}")
print(f"Q3: {grap['Q3']}")
print(f"Q4: {grap['Q4']}")
print(f"AXIS: {axis}")