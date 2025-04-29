def solution(nums:list) -> int:
    if 2*nums[1] == nums[2] + nums[0]:
        return 2*nums[-1] - nums[-2]
    return nums[-1] * (nums[1]/nums[0])