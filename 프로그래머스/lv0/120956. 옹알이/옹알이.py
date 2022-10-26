def solution(babbling):
    answer = 0
    check = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in range(4):
            if check[j] + check[j] in babbling[i]: continue
            if check[j] in babbling[i] : babbling[i] = babbling[i].replace(check[j], "")
    return babbling.count("")