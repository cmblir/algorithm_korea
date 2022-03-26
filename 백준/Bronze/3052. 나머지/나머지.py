B = []
result = []
for i in range(10):
    A = (int(input()) % 42)
    B.append(A)
    for i in B:
        if i not in result:
            result.append(i)
    
print(len(result))