import sys

def valid_ps(ps):
    x=0
    for p in ps:
        if p=='(':
            x += 1
        else:
            if not x: return 'NO'
            x -= 1
    if x!=0: return 'NO'
    return 'YES'

T = int(sys.stdin.readline())
for _ in range(T):
    print(valid_ps(sys.stdin.readline().strip()))