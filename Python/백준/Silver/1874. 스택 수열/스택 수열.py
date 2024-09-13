def output(x, y=None):
    global YN
    global push_st
    if x:
        for _ in range(y):
            st.append(push_st)
            YN+='+'
            push_st+=1
    else:
        ar.append(st.pop())
        YN+='-'

def stack(n):
    global YN
    if not st or st[-1] < n:
        if push_st > n: YN+='NO'
        elif push_st <= n:
            output(1, n+1 - push_st)
            output(0)
    elif st[-1]==n: output(0)
    elif st[-1] > n: YN+='NO'

N = int(input())
st, ar = [],[]
YN = ''
push_st = 1
for _ in range(N):
    n = int(input())
    stack(n)
    if 'NO' in YN:
        print('NO')
        break
if not 'NO' in YN: print(*YN,sep='\n')