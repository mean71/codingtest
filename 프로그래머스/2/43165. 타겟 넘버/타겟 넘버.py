# dfs
def solution(nums, target):
    global cnt
    cnt = 0
    def dfs(i, depth):
        global cnt
        if i==len(nums):
            if depth==target:
                cnt += 1
            return
        dfs(i+1,depth+nums[i])    
        dfs(i+1,depth-nums[i])
        return
    dfs(0,0)
    return cnt

# 조합 combinations
from itertools import combinations

def solution(nums, target):
    total = sum(nums)
    cnt = 0
    
    for i in range(len(nums)):
        for comb in combinations(nums, i):
            if total - 2*sum(comb) == target:
                cnt += 1
    return cnt
                
# 중복순열 product
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
