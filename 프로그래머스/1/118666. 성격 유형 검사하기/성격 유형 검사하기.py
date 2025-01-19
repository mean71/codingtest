def solution(survey, choices):
    mbti = {"R":0, "C":0, "J":0, "A":0,
                "T":0, "F":0, "M":0, "N":0}
    res = ""
    
    for s,c in zip(survey, choices):
        mbti[s[c>4]] += abs(c - 4)
    
    for a,b in (("R","T"), ("C","F"), ("J","M"), ("A","N")):
        res += max(a, b, key=lambda x:mbti[x])
    
    return res