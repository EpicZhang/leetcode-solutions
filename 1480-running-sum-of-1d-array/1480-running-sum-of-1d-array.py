class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i in range(len(nums)):
            the_sum = 0
            for j in range(i+1):
                the_sum += nums[j]
            runningSum.append(the_sum)
        return runningSum
            

        