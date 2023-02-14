def solution(array, n):
    array.sort()
    minValue = min(array, key=lambda x:abs(x-n))    
    return minValue
