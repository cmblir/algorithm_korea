import sys
N = int(sys.stdin.readline())
compare = []
for _ in range(N):
    compare.append(str(input()))
result = [i for i in compare[0]]
n = len(compare)
leng = len(compare[0])
for i in range(1, n):
    for j in range(leng):
        if result[j] != compare[i][j]:
            result[j] = "?"
print("".join(result))