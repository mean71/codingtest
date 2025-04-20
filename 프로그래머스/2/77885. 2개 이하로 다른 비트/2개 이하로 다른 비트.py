def solution(nums):
    return [1 + n + ((n ^ (n+1)) >> 2) for n in nums]