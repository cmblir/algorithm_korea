def solution(a, b, n):
    result = 0
    while n >= a:
        n -= a
        n += b
        result += b
    return result