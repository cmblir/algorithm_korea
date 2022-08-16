def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
        # 문자의 위치만큼 5의 제곱만큼 계산후에 -1을 해준다.
            # 5개 문자로 만들 수 있는 최대 숫자의 길이는 4이기 때문이기에 4로 나눠준다.
        # 이후에 AEIOU에서 해당 값을 검색한 뒤 + 1을 더해준다.
    return answer