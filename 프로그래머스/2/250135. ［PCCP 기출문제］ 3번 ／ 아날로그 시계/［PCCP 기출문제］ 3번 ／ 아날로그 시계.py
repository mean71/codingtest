def solution(h1, m1, s1, h2, m2, s2) -> int:
    '''
    args
        h1,m1,s1 (int): 시작시간 24h 00m 00s 
        h2,m2,s2 (int): 종료시간 24h 00m 00s
    return
        int: 초침과 시침 or 분침이 겹치는 "순간"의 횟수를 반환
    '''
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 + m2*60 + s2
    h, m, s = t1%43200, (m1*60 + s1)*12, s1*720
    cnt = int(s==h or s==m)
    
    for t in range(t1, t2):
        h, m, s = t%43200, t%3600 * 12, t%60 * 720
        
        if s < h <= s+719:
            cnt += 1
        if s < m <= s+708:
            cnt += 1
        if s+720 == h+1 and s+720 == m+12:
            cnt -= 1
    
    return cnt