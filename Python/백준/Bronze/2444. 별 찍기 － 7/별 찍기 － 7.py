N = int(input())
res = '*'
for i in range(N):
    print(' '*(N-i-1) + '*'*(i*2+1))
for i in range(N-1):
    print(' '*(1+i) + '*'*(2*N-3-i*2))