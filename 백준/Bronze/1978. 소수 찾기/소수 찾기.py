N = int(input())
a=0
for i in map(int,input().split()):
    c = 0
    for x in range(2, (i//2)+1):
        if not i%x: c+=1
    if not c and i > 1:
        a+=1
print(a)