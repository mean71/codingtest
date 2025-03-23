def solution(skill, skill_trees):
    skill = {k:v for v, k in enumerate(skill)}
    res = 0
    
    for trees in skill_trees:
        i = 0
        
        for sk in trees:
            if sk in skill:
                if i != skill[sk]:
                    break
                i += 1
        else:
            res += 1
    
    return res