def solution(nums):
    nums.sort()
    prime = set(range(2, (e:= sum(nums[-3::1]) + 1)))
    for x in range(2, e):
        if x in prime:
            n = 2
            while (y:= x*n) <= e:
                prime.discard(y)
                n += 1
    cnt = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                cnt += (nums[i] + nums[j] + nums[k] in prime)
    return cnt