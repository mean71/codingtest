def solution(players, callings):
    rank = {p:i for i, p in enumerate(players)}
    
    for call in callings:
        i = rank[call]
        players[i], players[i-1] = players[i-1], players[i]
        rank[players[i]], rank[players[i-1]] = rank[players[i-1]], rank[players[i]]
        
    return players