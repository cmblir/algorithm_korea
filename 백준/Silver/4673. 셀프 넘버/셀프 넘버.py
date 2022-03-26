num = set(range(1, 10001))
result = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    
    result.add(i)

self_num = sorted(num - result)
for i in self_num:
    print(i)