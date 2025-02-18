from itertools import combinations

def solution(nums, q, ans):
    '''
    args
        n(int): 1 - n 사이 서로 다른 정수 5개가 오름차순으로 정렬된 보안코드 10 <= n <= 30
        q(List[List[int]]): 입력한 정수 배열 1 <= len(q) == len(ans) <= 10
        ans(List[int]): 응답의 개수
    return
        res(int): 가능한 정수 조합 개수
    '''
    nums = set(range(1, nums+1))
    res = 0
    
    for i, n in enumerate(ans):
        if n == 0:
            for num in q[i]:
                nums.discard(num)
    
    for combi in map(set, combinations(nums, 5)):
        for i, comb in enumerate(q):
            if ans[i] != len(combi & set(comb)):
                break
        else:
            res += 1
    
    return res