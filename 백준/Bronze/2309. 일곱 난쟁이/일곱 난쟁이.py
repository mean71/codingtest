nine = [int(input()) for i in range(9)]
for i,x in enumerate(nine):
    for j,y in enumerate(nine[i+1:]):
        if sum(nine)-x-y == 100:
            nine.pop(i)
            nine.pop(i+j)
            break
for res in sorted(nine):
    print(res)