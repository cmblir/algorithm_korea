def solution(T):
    for i in range(T):
        K = list(map(str, input().split()))
        result = float(K[0])
        for i in K[1:]:
            if i == "@":
                result *= 3
            elif i == "%":
                result += 5
            elif i == "#":
                result -= 7
        print(f'{result:.2f}')

N = int(input())
solution(N)