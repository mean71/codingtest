n,k = map(int,input().split())
if k==n or k==0: 
    print(1)
else:
    def factorial(x):
        if x<2: return 1
        a = 1
        for i in range(2,x+1):
            a *= i
        return a
        
    print(factorial(n) // (factorial(k) * factorial(n-k)))