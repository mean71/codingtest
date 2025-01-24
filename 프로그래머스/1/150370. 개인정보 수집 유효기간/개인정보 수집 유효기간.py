def solution(today, terms, privacies):
    month, day = int(today[2:4])*12 + int(today[5:7]), today[-2:]
    terms = {term:int(m) for term, m in map(lambda s:s.split(), terms)}
    res = []
    
    for i, s in enumerate(privacies):
        m = int(s[2:4])*12 + int(s[5:7]) + terms[s[-1]]
        if m < month or m == month and day >= s[8:10]:
            res.append(i+1)
    
    return res