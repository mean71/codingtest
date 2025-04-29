def solution(nums:list) -> int:
    diff = nums[1] - nums[0]
    if diff + nums[1] == nums[2]:
        return nums[-1] + diff
    return nums[-1] * (nums[1]/nums[0])