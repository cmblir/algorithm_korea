n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for i in range(len(word) - 1): # 인덱스 범위 0 ~ -1까지
        if word[i] != word[i+1]: # 문자가 연속적이지 않을 경우
            new_word = word[i+1:] # 연속적이지 않은 문자 이후에 새로운 단어
            if new_word.count(word[i]) > 0: # 남은 문자열에 현재 글자가 있다면
                error += 1 # 그 값을 카운트해준다.
    if error == 0:
        group_word += 1 # 남은 문자열에 현재 글자가 없을 경우 +1을 해준다.
print(group_word)