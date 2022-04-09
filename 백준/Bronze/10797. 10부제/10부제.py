N = int(input())
A = map(int, input().split())
sum = 0
while N in A:
    sum += 1
print(sum)