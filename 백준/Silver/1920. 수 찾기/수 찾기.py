import sys
input = sys.stdin.readline
import collections as cl

A = cl.defaultdict(lambda:0)
N = int(input())
for key in map(int,input().split()):
    A[key] = 1
M = int(input())
for i in map(int,input().split()):
    print(A[i])