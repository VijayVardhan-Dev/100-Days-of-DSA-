class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        res = []
        for i in range(len(nums)):
            seen[nums[i]] = seen.get(nums[i],0)+1
            if seen[nums[i]] <= k:
                res.append(nums[i])
        return res

        