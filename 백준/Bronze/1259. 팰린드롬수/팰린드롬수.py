while (x:=input()) != '0':
    for i in range(len(x)//2):
        if x[i] != x[-i-1]:
            print('no')
            break
    else:
        print('yes')