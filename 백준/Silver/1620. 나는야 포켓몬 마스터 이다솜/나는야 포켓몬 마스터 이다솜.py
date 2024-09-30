import sys

N, M = map(int, sys.stdin.readline().split())

poket_dic = {}
for i in range(1,N+1):
    poketmon = sys.stdin.readline().strip('\n')
    poket_dic[poketmon] = i
    poket_dic[str(i)] = poketmon
for _ in range(M):
    print(poket_dic[sys.stdin.readline().strip('\n')])