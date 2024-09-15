T = int(input())
dic = {0:0, 1:1, '0':1, '1':0}
for i in range(T):
    N = int(input())
    for i in range(2,N+1):
        dic[i] = dic[i-1] + dic[i-2]
        dic[str(i)] = dic[str(i-1)] + dic[str(i-2)]
    print(dic[str(N)], dic[N])