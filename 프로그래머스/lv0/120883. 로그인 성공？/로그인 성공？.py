def solution(id_pw, db):
    for idx in db:
        if id_pw[0] == idx[0]:
            if id_pw[1] == idx[1]: return "login"
            else: return "wrong pw"
        else: pass
    return "fail"