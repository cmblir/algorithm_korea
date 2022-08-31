def solution(survey, choices):
    '''
    Rion, Tube
    Corn, Frodo
    JayZ, Muzi
    Apeach, Neo
    '''
    answer = ''
    lst = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    score = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }
    for item, choice in zip(survey, choices):
        if choice < 4:
            score[item[0]] += (4 - choice)
        elif choice > 4:
            score[item[1]] += (choice - 4)
            
    for idx in lst:
        if score[idx[0]] >= score[idx[1]]: answer += idx[0]
        else:
            answer += idx[1]
    return answer