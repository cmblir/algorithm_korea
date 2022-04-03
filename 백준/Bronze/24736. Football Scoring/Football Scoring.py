for i in range(2):
    result = 0
    T, F, S, P, C = map(int, input().split())
    result += (T * 6) + (F * 3) + (S * 2) + (P * 1) + (C * 2)
    print(result)