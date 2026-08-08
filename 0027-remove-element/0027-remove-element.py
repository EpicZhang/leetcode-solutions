class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        if nums.count(val) == 0:
            return k
        else:
            for i in range(nums.count(val)):
                nums.remove(val)
                nums.append(val)
            return k
        
        