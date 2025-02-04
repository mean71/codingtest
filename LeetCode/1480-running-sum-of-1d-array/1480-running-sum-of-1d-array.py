class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)): nums[i] = nums[i] + nums[i-1]; return nums
        # return [sum(nums[i-len(nums)::-1])for i in range(len(nums))] # Time: O(N^2), Space: O(N)