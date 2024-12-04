def solution(lottos, Ns):
    win_n = len(set(lottos)&set(Ns))
    zero = lottos.count(0)
    x = x if (x:=(7 - win_n - zero)) < 6 else 6
    y = y if (y:=(7 - win_n)) < 6 else 6
    return [x,y]