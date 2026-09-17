class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Map={}
        for i, n in enumerate(nums):
            complement = target - n
            #if complement alr in map, return
            if complement in Map:
                return [Map[complement], i]
        #add complement 
            Map[n] = i
