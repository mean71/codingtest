def solution(n):
    nums = set(range(2,n+1))
    for i in range(2, n+1):
        if i in nums:
            x = 2
            while i*x <= n:
                nums.discard(i*x)
                x += 1
    return len(nums)