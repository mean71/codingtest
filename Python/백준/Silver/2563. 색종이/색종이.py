import sys

n, extent = int(sys.stdin.readline()), []

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    extent += [ (a+i+1,b+j+1) for i in range(10) for j in range(10)]
    
print(len(set(extent)))