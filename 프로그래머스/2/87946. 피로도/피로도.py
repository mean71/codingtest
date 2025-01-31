from itertools import permutations

def solution(k, dungeons):
    res = 0
    
    for perm in permutations(d for d in dungeons if d[0] <= k):
        cur_k = k
        cnt = 0
        
        for min_k, consum_k in perm:
            if cur_k >= min_k:
                cur_k -= consum_k
                cnt += 1
            else:
                break
        
        res = max(res, cnt)
    
    return res