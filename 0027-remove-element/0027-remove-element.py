# Time complexity: O(n^2)
# Space complexity: O(1)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = len(nums) - nums.count(val)
#         if nums.count(val) == 0:
#             return k
#         else:
#             for i in range(nums.count(val)):
#                 nums.remove(val)
#                 nums.append(val)
#             return k

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k
       




        
        