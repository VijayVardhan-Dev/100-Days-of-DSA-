class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sum1 = 0
        l = 0
        for i in range(k):
            sum1 += nums[i]

        min_s = sum1/k
        
        for j in range(k,len(nums)):
            sum1 -= nums[l]
            sum1 = sum1 + nums[j]
            l+=1

            if sum1/k > min_s:
                min_s = sum1/k

        return min_s


        

