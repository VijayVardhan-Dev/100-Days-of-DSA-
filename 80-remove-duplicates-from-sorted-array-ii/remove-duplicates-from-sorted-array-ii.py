class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        i = 0
        while i < len(nums):
            if nums[i] not in seen:
                seen[nums[i]] = 1
                i += 1
            elif seen[nums[i]] < 2:     
                seen[nums[i]] += 1
                i += 1
            else:
                nums.pop(i) 
        return len(nums)
            
            
        