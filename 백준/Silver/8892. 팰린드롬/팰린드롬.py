import sys
input = sys.stdin.readline

def check(word):
    for i in range(len(word)//2):
        if word[i]!=word[-i-1]:
            return None
    return word

for _ in range(int(input())):
    words = []
    res = 0
    for _ in range(k:=int(input())):
        words.append(input().strip())

    for i,x in enumerate(words[:len(words)-1]):
        for y in words[i+1:]:
            if res:=check(x+y):
                print(res)
                break
            if res:=check(y+x):
                print(res)
                break
        else:continue
        break
    if not res:
        print(0)