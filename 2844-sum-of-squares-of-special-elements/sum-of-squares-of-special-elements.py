class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ssum = 0
        n = len(nums)
        for i in range(n):
            if  n % (i+1) == 0:
                ssum += nums[i] ** 2
        return ssum
        