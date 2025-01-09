from collections import Counter

def solution(player, completion):
    player = Counter(player)
    
    for p in completion:
        if player[p] != 1:
            player[p] -= 1
        else: del player[p]
        
    return list(player)[0]