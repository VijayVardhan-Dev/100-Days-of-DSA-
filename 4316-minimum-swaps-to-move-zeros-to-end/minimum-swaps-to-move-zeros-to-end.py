class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        N = len(nums)
        r = N-1
        l = 0
        count = 0
        while l < r:
            if nums[l] == 0:
                while r > l and nums[r] == 0:
                    r -= 1
                if r > l:
                    nums[l],nums[r] = nums[r],nums[l]
                    count += 1
            l += 1
        return count   