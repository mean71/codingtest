def solution(players, callings):
    rank = {k:i for i,k in enumerate(players)}
    
    for call in callings:
        i = rank[call]
        rank[players[i]] -= 1
        rank[players[i-1]] += 1
        players[i], players[i-1] = players[i-1], players[i]
    
    return players