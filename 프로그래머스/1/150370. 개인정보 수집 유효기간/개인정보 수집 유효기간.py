def solution(today, terms, privacies):
    month, day = int(today[2:4])*12 + int(today[5:7]), today[-2:]
    terms = {s[0]: int(s[2:]) for s in terms}
    res = []
    
    for i, s in enumerate(privacies):
        m = int(s[2:4])*12 + int(s[5:7]) + terms[s[-1]]
        if m < month or m == month and day >= s[8:10]:
            res.append(i+1)
    
    return res