A, B, C = map(int, input().split())
if A >= B and A <= C or A >= C and A <= B:
    print(A)
elif B >= C and B <= A or B >= A and B <= C:
    print(B)
else:
    print(C)