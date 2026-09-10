class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i],0) + 1

        for i in seen:
            if seen[i] == 1:
                return i
            
        
