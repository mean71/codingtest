import sys
T = int(input())
for i in range(T):
    OX = sys.stdin.readline()
    combo,score = 0,0
    for j in OX:
        if j == 'O':
            combo+=1
            score+=combo
        else:
            combo = 0
    print(score)