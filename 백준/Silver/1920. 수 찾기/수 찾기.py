import sys
input = sys.stdin.readline  

([print(D.get(i,0))for i in input().split()]if(N:=input())and(D:={k:1 for k in set(input().split())})and(M:=input())else 0)