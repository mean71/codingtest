import sys
input = sys.stdin.readline
# s2 2805번 나무 자르기
# 이분탐색
N,M = map(int, input().split())
trees = list(map(int, input().split()))
# 이분탐색 포인트 초기화
l,r = 0,max(trees)

while l <= r: # 유효조건 # 종료시점: l은 r보다 커진다
    h = (l+r)//2 # a + (a+1) -> a # //2 지점으로 이분탐색
    wood = sum(tree-h for tree in trees if h < tree)

    if wood >= M: # 잘린 나무길이가 충분한가
        l = h + 1 # 더 적게 잘라가기 위해 높이 증가 
    else: 
        r = h - 1 # 더 많이 잘라가기 위해 높이 감소
print(r) # r -> wood < M: 의 마지막 시점으로 고정: 높이의 최댓값