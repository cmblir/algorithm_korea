import sys
input = sys.stdin.readline
def solution(n):
    result = []
    for i in range(n):
        result.append(str(input().strip()))
    tmp = set(result)
    result = list(tmp)
    result.sort()
    result.sort(key = len)
    for i in result:
        print(i)
solution(int(input()))