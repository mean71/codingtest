solution=lambda N:[i for i in range(2,N//2+1)if N%i==0 and all(i%j for j in range(2,int(i**0.5)+1))]or[N]