N,B = map(int, input().split())
alpha,dic,res = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",{},''
for i in zip([x for x in range(10,36)],alpha):
    dic[i[0]] = i[1]
while N:
    if N%B > 9:
        res = dic[N%B] + res
    else:
        res = str(N%B) + res
    N = N//B
print(res)