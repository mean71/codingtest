def solution(lottos, Ns):
    rank =[6,6,5,4,3,2,1]
    win_n = len(set(lottos)&set(Ns))
    zero = lottos.count(0)
    return rank[win_n+zero], rank[win_n]