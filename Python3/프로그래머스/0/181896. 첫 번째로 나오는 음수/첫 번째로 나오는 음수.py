def solution(nl):
    for i,x in enumerate(nl):
        if x<0: return i 
    return -1