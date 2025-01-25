N = int(input())

if 0<N<101:
    for n in range(N):
        print(' '*(N-n-1)+'*'*(n+1))