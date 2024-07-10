sumoney = 0
while sumoney == 0 :
    X = int(input())
    N = int(input())
    if 1 <= X <= 1000000000 and 1 <= N <= 100:
        for n in range(N):        
            a,b = map(int, input().split())
            if 1 <= a <= 1000000 and 1 <= b <= 10:
                pass
            else:
                continue
            sumoney += a*b
        if sumoney == X:
            print('Yes')
        else:
            print('No')
    else:
        continue