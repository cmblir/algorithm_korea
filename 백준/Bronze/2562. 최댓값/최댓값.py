max = 0
num = 0
for i in range(9):
    A = int(input())
    if max < A:
        max = A
        num = i + 1
print(max)
print(num)