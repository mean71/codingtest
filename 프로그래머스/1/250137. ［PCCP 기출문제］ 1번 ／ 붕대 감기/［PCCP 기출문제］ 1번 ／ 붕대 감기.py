def solution(heal, health, attacks):
    hp = health
    time = 0
    for t, atk in attacks:
        if atk >= health:
            return -1
        n = t-time-1
        hp = min(health, hp + n*heal[1] + (n//heal[0])*heal[2]) - atk
        if hp <= 0:
            return -1        
        time = t
    return hp