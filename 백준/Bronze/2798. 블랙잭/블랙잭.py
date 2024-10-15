# b2 2798번 블랙잭
N, M = map(int, input().split())
cards = list(map(int, input().split()))
res = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if res < (s:=sum((cards[i],cards[j],cards[k]))) <= M:
                res = s
print(res)