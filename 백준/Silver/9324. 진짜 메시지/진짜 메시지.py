import sys
input = sys.stdin.readline

def check(s):
    cnt = {}
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        cnt[c] = cnt.get(c, 0) + 1
        
        if cnt[c] == 3:
            if i == len(s) or s[i] != c:
                return "FAKE"
            cnt[c] = 0
            i += 1
        
    return "OK"

for _ in range(int(input())):
    print(check(input().rstrip()))