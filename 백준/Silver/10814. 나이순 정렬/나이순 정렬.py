x = [input().split()+[i] for i in range(int(input()))]
for r in sorted(x, key=lambda z:(int(z[0]),z[2])):
    print(f'{r[0]} {r[1]}')