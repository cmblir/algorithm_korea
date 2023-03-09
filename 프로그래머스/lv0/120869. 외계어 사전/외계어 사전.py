def solution(spell, dic):
    spell = set(spell)
    for idx in dic:
        if not spell-set(idx):
            return 1
    return 2