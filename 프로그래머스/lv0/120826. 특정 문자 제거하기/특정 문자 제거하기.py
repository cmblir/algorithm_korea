def solution(my_string, letter):
    result = [i for i in my_string if i != letter]
    return "".join(result)