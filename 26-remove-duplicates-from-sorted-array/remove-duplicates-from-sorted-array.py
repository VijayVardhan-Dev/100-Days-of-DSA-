class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        for r in range(1,n):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l+1
            
        