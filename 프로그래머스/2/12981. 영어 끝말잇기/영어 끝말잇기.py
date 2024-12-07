def solution(N, L):
    words, ec = set(), ""

    for i,s in enumerate(L):
        if i and (ec!=s[0] or s in words):
            return [i%N + 1, i//N + 1]
        words.add(s)
        ec = s[-1]
        
    else: return [0, 0]