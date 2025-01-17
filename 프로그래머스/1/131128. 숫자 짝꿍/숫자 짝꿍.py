from collections import Counter

def solution(X, Y):
    num_n = Counter(X)&Counter(Y)
    num = sorted(Counter(X)&Counter(Y), reverse=True)

    if len(num)==1 and num[0]=="0":
        return "0"
    
    return "".join(str(n)*num_n[str(n)] for n in num) or "-1"