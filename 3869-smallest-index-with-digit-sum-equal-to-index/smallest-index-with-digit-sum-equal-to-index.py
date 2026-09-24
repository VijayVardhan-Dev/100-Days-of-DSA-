class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            dsum = 0
            while nums[i] > 0:
                rem = nums[i] % 10
                dsum += rem
                nums[i] = nums[i]//10
            if dsum == i:
                return i
        return -1
        