def solution(keyinput, board):
    cur = [0, 0]
    x, y = board[0]//2, board[1]//2
    for k in keyinput:
        if k=="up" and cur[1] < y:
            cur[1] += 1
        elif k=="down" and cur[1] > -y:
            cur[1] -= 1
        elif k=="right" and cur[0] < x:
            cur[0] += 1
        elif k=="left" and cur[0] > -x:
            cur[0] -= 1
    return cur