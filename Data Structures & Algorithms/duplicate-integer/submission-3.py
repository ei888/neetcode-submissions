class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dash = set(nums)
        if len(nums_dash) == len(nums):
            return False
        return True