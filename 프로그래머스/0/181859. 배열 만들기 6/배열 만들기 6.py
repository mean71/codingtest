def solution(L):
    return(stk:=[])or[stk.pop()if stk and i==stk[-1]else stk.append(i)for i in L]and(stk or[-1])