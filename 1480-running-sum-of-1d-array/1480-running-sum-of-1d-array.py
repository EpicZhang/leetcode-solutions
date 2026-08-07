# Time complexity: O(n^2)
# Space complexity: O(n)
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         runningSum = []
#         for i in range(len(nums)):
#             the_sum = 0
#             for j in range(i+1):
#                 the_sum += nums[j]
#             runningSum.append(the_sum)
#         return runningSum

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        the_sum = 0
        for i in range(len(nums)):
            the_sum += nums[i]
            runningSum.append(the_sum)
        return runningSum
            


        