A, B, C = map(int, input().split())
cost = 0

if A == B == C:
    cost += 10000 + (A * 1000)
elif A == B or A == C:
    cost += 1000 + (A * 100)
elif B == C:
    cost += 1000 + (B * 100)
else:
    if A > B and A > C:
        cost += (A * 100)
    elif B > C and B > A:
        cost += (B * 100)
    else:
        cost += (C * 100)
    
print(cost)