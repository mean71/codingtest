T = int(input())

for _ in range(T):
    H,W,N = map(int, input().split())
    if N <= H*W:
        floor = N%H if N%H else H
        room = 1+(N-1)//H
        print(f'{floor}{room:02d}')