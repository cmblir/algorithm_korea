def solution(prices):
    # 반복문이 도는 동안 1초씩 증가함
    n = len(prices)
    result = [0] * n
    stack = []
    for idx, price in enumerate(prices):
        while len(stack) != 0 and price < prices[stack[-1]]:
            tmp = stack.pop()
            result[tmp] = idx - tmp
        stack.append(idx)
    
    while len(stack) != 0:
        tmp = stack.pop()
        result[tmp] = n - 1 - tmp

    return result