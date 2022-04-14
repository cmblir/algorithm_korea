# 탑다운 방식
def fib(N, mem): 
    if N == 0: # N이 0인 경우 
        mem[N] = [1, 0]
        return mem[N]
    elif N == 1: # N이 1인 경우 
        mem[N] = [0, 1]
        return mem[N]
    if N in mem: # 메모리제이션에 값이 있을 경우
        return mem[N]
    else:
        a = fib(N -1, mem)[0] + fib(N -2, mem)[0]
        b = fib(N -1, mem)[1] + fib(N -2, mem)[1]
        mem[N] = [a,b]
        return mem[N]

def memo(N): # 메모리제이션 함수 선언
    mem = {}
    return fib(N, mem)
    
T = int(input())
for i in range(T):
    N = int(input())
    f = memo(N)
    print(f[0], f[1])