A = list(map(int, input().split()))
if A == sorted(A): # 정렬된 값이 맞다면
    print('ascending')
elif A == sorted(A, reverse=True): # 역정렬이 맞다면
    print('descending')
else:
    print('mixed')