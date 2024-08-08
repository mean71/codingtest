br='()'
def condition(s):
    if 0 <= len(s) <= 100000 and ' ' not in s and all(s in br for i in s):
        return True
def solution(s):
    x=0
    for i in range(len(s)):
        if s[i] == '(':
            x+=1
        else:
            x-=1
            if x<0:
                return False
    if x == 0 : return True
    return False