def solution(numbers):
    numbers.sort()
    maximum = numbers[-1] * numbers[-2]
    minimum = numbers[0] * numbers[1]
    return max(maximum, minimum)