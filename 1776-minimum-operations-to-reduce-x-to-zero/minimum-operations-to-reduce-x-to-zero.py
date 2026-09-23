class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        l = r = 0
        winsum = 0
        min_op = -1
        while r < len(nums):
            winsum += nums[r]
            r += 1
            if winsum > target:
                while l < r and winsum > target:
                    winsum -= nums[l]
                    l += 1
            if winsum == target:
                min_op = max(min_op , r - l)

        return len(nums) - min_op if min_op != -1 else -1