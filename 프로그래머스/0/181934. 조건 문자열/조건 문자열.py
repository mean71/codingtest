solution=lambda ineq,eq,n,m:int((n==m)&(eq=="=")|(n>m)&(ineq==">")|(n<m)&(ineq=="<"))
solution=lambda ineq,eq,n,m:eval(str(n)+ineq+(eq=="=")*eq+str(m))/1