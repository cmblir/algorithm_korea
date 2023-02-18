import re
def solution(my_string):
    result = re.findall(r'\d+', my_string)
    result = [int(i) for i in result]
    return sum(result)