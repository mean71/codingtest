class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[i-len(nums)::-1])for i in range(len(nums))]