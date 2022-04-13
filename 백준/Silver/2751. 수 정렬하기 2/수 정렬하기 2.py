# O(n) sorted로 구현
import sys
n = int(input())
result = []
for _ in range(n):
    result.append(int(sys.stdin.readline()))
for i in sorted(result):
    sys.stdout.write(str(i)+'\n')