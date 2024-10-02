import sys
import collections as cl

T=int(sys.stdin.readline())
for _ in range(T):
    N,M=map(int, sys.stdin.readline().split())
    W=cl.deque([i for i in enumerate( map(int, sys.stdin.readline().split()) )])
    turn=1
    while True:
        if W[0][1] < max(j[1] for j in W):
            W.append(W.popleft())
        else:
            if W[0][0]==M:
                print(turn)
                turn=1
                break
            else:
                W.popleft()
                turn+=1