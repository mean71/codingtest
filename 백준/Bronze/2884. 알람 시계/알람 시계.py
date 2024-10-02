H,M=map(int,input().split())
def time(H,M):
    if M >= 45:
        M = M - 45
    elif M < 45:
        M += 15
        if H > 0:
            H -= 1
        elif H == 0:
            H=23
    return f'{H} {M}'    
print(time(H,M))