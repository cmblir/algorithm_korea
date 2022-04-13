T = int(input())
test = []
for i in range(T):
    N = int(input())
    test.append(N)
n = len(test)
for j in range(n):
    for h in range(j+1, n):
        if test[j] > test[h]:
            test[j], test[h] = test[h], test[j]

for k in test:
    print(k)