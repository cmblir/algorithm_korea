N = str(input())

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro:
    N = N.replace(i, '*')

print(len(N))