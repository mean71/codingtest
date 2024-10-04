import sys
import collections as cl
N = int(sys.stdin.readline())
Nc = [i for i in map(int, sys.stdin.readline().split())]
M = int(input())
dic = cl.Counter(Nc)
for k in map(int, sys.stdin.readline().split()):
    print(dic[k],end=' ')