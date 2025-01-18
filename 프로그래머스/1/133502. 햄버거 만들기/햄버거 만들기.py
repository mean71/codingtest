def solution(ingredient):
    stack = ingredient[0:3]
    res = 0
    
    for n in ingredient[3:]:
        stack.append(n)
        if stack[-4:]==[1,2,3,1]:
            del stack[-4:]
            res += 1
    
    return res