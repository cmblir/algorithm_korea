import math
N = int(input())
A = N - (N * 0.22)
B = N - ((N * 0.2) * 0.22)
print(math.floor(A), math.floor(B))