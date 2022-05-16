import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    name, num = map(str, input().split())
    lst.append([name, int(num)])
lst.sort(key = lambda x : x[1])
print(lst[0][0])