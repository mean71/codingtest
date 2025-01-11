def solution(s, query):
    res = list(s)
    for s, e in query:
        res[s:e+1] = res[s:e+1][::-1]
    return ''.join(res)