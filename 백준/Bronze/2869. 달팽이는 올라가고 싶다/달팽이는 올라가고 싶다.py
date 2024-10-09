A,B,V = map(int, input().split())
if V==A:print(1)
else:
    print(1+(V-A)//(A-B)+bool((V-A)%(A-B)))