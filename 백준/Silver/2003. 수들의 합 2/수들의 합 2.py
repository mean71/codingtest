# s4 2003번 수들의 합 2
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
l = r = 0
nsum = 0
res = 0


while r < N:
    if nsum < M: # 다음거 더한다
        if nums[r] > M: # M 보다 큰 수가 나오면 다음 인덱스부터시작하도록 초기화
            l = r = r+1
            nsum = 0
            continue
        elif nums[r]==M:
            l = r = r+1
            nsum = 0
            res += 1
            continue
        nsum += nums[r]
        r += 1
    elif nsum > M:  #이전걸 뺀다
        nsum -= nums[l]
        l += 1
    if nsum == M: #nsum == M 경우의수를 하나더하고 이전걸 뺀다
        res += 1
        nsum -= nums[l]
        l = l+1
print(res)