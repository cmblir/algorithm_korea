str = input()
answer = lambda x: x.lower() if x.isupper() else x.upper()
print(''.join([answer(i) for i in str]))