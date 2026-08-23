class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx = max(nums)
        mn = min(nums)
        seen = set(nums)
        result = []
        for i in range(mn,mx):
            if i not in seen:
                result.append(i)
        return result
