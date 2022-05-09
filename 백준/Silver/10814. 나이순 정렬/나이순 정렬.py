import sys
input = sys.stdin.readline
N = int(input())
user = []
for i in range(N):
    age, name = list(map(str, input().split()))
    age = int(age)
    user.append((age, name))
user = sorted(user, key = lambda x : x[0])
for i in user:
    print(i[0], i[1])