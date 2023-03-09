def solution(spell, dic):
    result = 0
    for idx in dic:
        spell = {string: 0 for string in spell}
        for i in idx:
            if i in spell.keys(): spell[i] += 1
        cnt = 0
        for j in spell.values():
            if j >= 1: cnt += 1
        if cnt >= len(list(spell.keys())) : result += 1
    if result >= 1: return 1
    else: return 2