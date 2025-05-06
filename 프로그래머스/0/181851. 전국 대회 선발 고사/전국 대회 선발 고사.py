def solution(rank:list, attendance:list) -> int:
    runner = sorted((i for i, atten in enumerate(attendance) if atten), key=lambda x:rank[x])
    return runner[0]*10000 + runner[1]*100 + runner[2]