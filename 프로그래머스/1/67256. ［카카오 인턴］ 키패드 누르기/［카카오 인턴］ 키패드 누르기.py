def solution(num, hand):
    res = ""
    cur = ["*","#"]
    for n in num:
        if n in {1,4,7}:
            res += "L"
            cur[0] = n
        elif n in {3,6,9}:
            res += "R"
            cur[1] = n
        else:
            ni = (2,5,8,0).index(n)
            
            if cur[0] in {2,5,8,0}:
                l = abs(ni - (2,5,8,0).index(cur[0]))
            else:
                l = abs(ni - (1,4,7,"*").index(cur[0])) + 1
            
            if cur[1] in {2,5,8,0}:
                r = abs(ni - (2,5,8,0).index(cur[1]))
            else:
                r = abs(ni - (3,6,9,"#").index(cur[1])) + 1
            
            res += ("L", "R")[l > r or l==r and hand=="right"]
            cur[l > r or l==r and hand=="right"] = n
    
    return res