import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))
res = [0]*N
receive = []
for i, h in enumerate(height):
    while receive and h > height[receive[-1]]:
        receive.pop()
    
    if receive:
        res[i] = receive[-1] + 1
    
    receive.append(i)

print(*res)