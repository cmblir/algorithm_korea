def solution(food):
    result = ""
    for idx, cnt in enumerate(food):
        result += str(idx) * (cnt // 2)
    return result + "0"*food[0] + result[::-1]