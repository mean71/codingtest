def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for rsv in set_reserve:
        
        if rsv-1 in set_lost:
            set_lost.remove(rsv-1)
            
        elif rsv+1 in set_lost:
            set_lost.remove(rsv+1)
        
    return n - len(set_lost)