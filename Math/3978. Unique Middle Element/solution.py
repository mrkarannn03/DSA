class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        target_index = (len(nums) // 2) 
        return True if nums.count(nums[target_index]) == 1 else False
