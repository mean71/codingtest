N = int(input())
xy = []
for i in range(N):
    x,y = map(int, input().split())
    xy.append((x,y))
for i,j in sorted(xy):
    print(i,j)