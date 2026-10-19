class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ssum = 0
        n = len(nums)
        for i in range(1,n+1):
            if n > 0 and n % i == 0:
                ssum += nums[i-1] * nums[i-1]
        return ssum
        