# Time Complexity: O(n log n)
# Space Complexity: O(n)

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         return ((nums[-1] - 1) * (nums[-2] - 1))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = second = 0
        for i in nums:
            if i > largest:
                second = largest
                largest = i
            elif i > second:
                second = i
        return (largest - 1) * (second - 1)
        