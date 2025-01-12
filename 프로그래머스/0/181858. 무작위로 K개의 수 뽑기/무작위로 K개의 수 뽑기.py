def solution(arr, k):
    res = []
    n_set = set()
    
    for n in arr:
        if len(res) != k and n not in n_set:
            res.append(n)
            n_set.add(n)
    
    return res + [-1]*(k - len(res))