N = int(input())

num = 1

while N > num:
    N -= num
    num += 1

if num % 2 == 0:
    a = N
    b = num - N + 1
else:
    a = num - N + 1
    b = N

print(f'{a}/{b}')