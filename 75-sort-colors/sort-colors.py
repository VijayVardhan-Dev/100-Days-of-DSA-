class Solution:
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        l = 0
        r = N-1
        for i in range(N):
            
            while r > i and nums[i] == 2:
                nums[r],nums[i] = nums[i],nums[r]
                r -= 1
            if (nums[i] == 0):
                nums[l],nums[i] = nums[i],nums[l]
                l += 1



        """
        Do not return anything, modify nums in-place instead.
        """
        