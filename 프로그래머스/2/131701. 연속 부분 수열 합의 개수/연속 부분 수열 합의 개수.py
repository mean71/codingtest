def solution(elem):
    res = set()
    length = len(elem)
    
    for n in range(1, length + 1):
        sub_sum = sum(elem[0:n])
        res.add(sub_sum)
        
        for s in range(1, length):
            sub_sum += (elem[(s+n-1)%length] - elem[s])
            res.add(sub_sum)
            
    return len(res)