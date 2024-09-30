import collections as cl
import sys
input = sys.stdin.readline

M,N= map(int, input().split())
if M<=2<=N:print(2)

decimal = cl.defaultdict(bool)
decimal[0]=decimal[1]=True

for i in range(3, N+1, 2):
    if not decimal[i]:
        if M<= i <= N:
            print(i)
        for j in range(i+i*2, N+1, i*2):
                decimal[j]=True