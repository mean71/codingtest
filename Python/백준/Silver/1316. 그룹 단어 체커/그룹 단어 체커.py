N = int(input())
for i in range(N):
    words = input()
    r=set()
    temp = ''
    for j in words:
        if not temp:
            temp = j
            r.add(j)
            continue
        if temp == j:
            continue
        elif temp != j:
            if j in r:
                N-=1
                break
            else:
                temp = j
                r.add(j)
print(N)