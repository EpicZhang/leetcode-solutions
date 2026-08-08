# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = 0
        for i in range(len(nums)):
            nums_sum += nums[i]
        left_sum = 0
        if nums_sum - nums[0] == 0:
            return 0
        nums_sum -= nums[0]
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            nums_sum -= nums[i]
            if left_sum == nums_sum:
                return i 
        return -1
 


                

            
            
        