import re
def solution(polynomial):
    x_number, number = 0, 0
    for poly in polynomial.split(" + "):
        if poly.isnumeric(): number += int(poly)
        else:
            if poly == "x": x_number += 1
            else: x_number += int(re.sub(r'[^0-9]', '', poly))
    if x_number == 1: x_number = ""
    if number == 0 and x_number == 0: return "0"
    if x_number == 0: return str(number)
    if number == 0: return f"{x_number}x"
    return f"{x_number}x + {number}"