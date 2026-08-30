class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        min_indx = nums.index(min(nums))
        max_indx = nums.index(max(nums))
        l = min(min_indx,max_indx) 
        r = max(min_indx,max_indx) 
        return min((l+1)+(N-r),r+1,N-l)