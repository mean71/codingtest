class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num:
            num = num//(2-num%2)-num%2
            step += 1
        return step