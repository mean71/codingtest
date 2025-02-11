import sys
from typing import List
input = sys.stdin.readline
def test(depth:int=0, check:List[int]=[], score:int=0):
    global cnt
    if depth==10:
        cnt += 1
        return
    
    for i in range(1, 6):
        if depth >= 2 and i == check[-1] == check[-2]:
            continue

        if i == answer[depth]:
            test(depth+1, check[-1::]+[i], score+1)
        else:
            if depth - score >= 5:
                continue
            test(depth+1, check[-1::]+[i], score)

answer: List[int] = list(map(int, input().split()))
cnt = 0

test()
print(cnt)