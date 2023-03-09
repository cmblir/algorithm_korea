def solution(keyinput, board):
    w_center = board[0]//2
    h_center = board[1]//2
    a = {
        "w" : 0,
        "h" : 0
    }
    for idx in keyinput:
        if idx == "left" :
            if a["w"] > -w_center:
                a["w"] -= 1
        elif idx == "right" :
            if a["w"] < w_center:
                a["w"] += 1
        elif idx == "up" : 
            if a["h"] < h_center:
                a["h"] += 1
        elif idx == "down" :
            if a["h"] > -h_center:
                a["h"] -= 1
    return [a["w"], a["h"]]