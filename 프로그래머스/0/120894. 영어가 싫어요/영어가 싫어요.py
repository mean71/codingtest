def solution(n):
    dic = {"zero":"0","one":"1","two":"2","three":"3","four":"4",
           "five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    return (s:=0) or int("".join(x for e in range(3,len(n)+1) if (x:=dic.get(n[s:e])) and (s:=e)))