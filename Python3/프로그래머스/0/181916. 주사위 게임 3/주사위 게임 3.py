def solution(a, b, c, d):
    x=[a,b,c,d]
    if len(set(x))==1: return 1111*a
    elif len(set(x))==4: return min(x)
    elif a==b and c==d: return (a+c)*abs(a-c)
    elif a==c and b==d: return (a+b)*abs(a-b)
    elif a==d and b==c: return (a+b)*abs(a-b)
    
    elif len(set(x))==2:
        return (10*[x[i] for i in range(4) if x.count(x[i])==3 ][0] + [x[i] for i in range(4) if x.count(x[i])==1][0])**2
    elif len(set(x))==3:
        y = [x[i] for i in range(4) if x.count(x[i])==1]
        return y[0]*y[1]    
'''
a b c d min(x)
p p p p 1111*p

p p q q (p+q)*abs(p-q)
p p p q (10*p+q)**2
p p q r q*r
'''