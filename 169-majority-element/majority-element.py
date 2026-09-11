class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        return max(seen,key = seen.get)
        