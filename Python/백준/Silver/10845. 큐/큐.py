import sys

N = int(input())
Q = []
for i in range(N):
    A = sys.stdin.readline().split()

    if A[0] == 'pop':
        if len(Q) != 0: print(Q.pop(0))
        else: print('-1')

    elif A[0] == 'size': print(len(Q))

    elif A[0] == 'empty':
        if len(Q) == 0: print('1')
        else: print('0')

    elif A[0] == 'front':
        if len(Q) != 0: print(Q[0])
        else: print('-1')

    elif A[0] == 'back':
        if len(Q) != 0: print(Q[-1])
        else: print('-1')
    
    else: Q.append(A[1])