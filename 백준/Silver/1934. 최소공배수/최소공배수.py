import sys
T = int(sys.stdin.readline())
# 최소 공배수 문제 : 유클리드 호제법 활용

# 최대공약수 구하기
def GCD(x, y):
    while(y): # y가 참일때 = 자연수 일때 = a % b != 0
        x, y = y, x % y
    return x

# 최소공배수 구하는 공식
def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(LCM(A, B))