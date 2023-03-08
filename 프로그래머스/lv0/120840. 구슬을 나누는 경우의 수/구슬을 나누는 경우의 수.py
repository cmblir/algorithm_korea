from math import factorial as fact
def solution(balls, share):
    n = fact(balls)
    m = fact(share)
    n_m = fact(balls-share) * m
    return n/n_m