A, B = map(int, input().split())
result_A = []
result_B = []
for a in str(A):
    result_A.append(a)
for b in str(B):
    result_B.append(b)
result_A.reverse()
result_B.reverse()
num_A = "".join(result_A)
num_B = "".join(result_B)
if num_A > num_B:
    print(num_A)
else:
    print(num_B)