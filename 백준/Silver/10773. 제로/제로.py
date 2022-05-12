import sys
input = sys.stdin.readline
K = int(input())
# 스택으로 해결
stack = []
for _ in range(K):
    money = int(input())
    if money != 0: stack.append(money)
    else: stack.pop()
print(sum(stack))