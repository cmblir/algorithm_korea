def gcd(a, b):
    while b != 0: a, b = b , a % b
    return a
def solution(numer1, denom1, numer2, denom2):
    lcm = (denom1 * denom2) // gcd(denom1, denom2)
    num3 = numer1 * (lcm // denom1)
    num4 = numer2 * (lcm // denom2)
    result_num = num3 + num4
    result_denom = lcm
    divisor = gcd(result_num, result_denom)
    return result_num // divisor, result_denom // divisor