class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        window = set()
        l = 0

        for r in range(N):

            if nums[r] in window:
                return True
            window.add(nums[r])

            if r - l >= k:
                window.remove(nums[l])
                l += 1
                
        return False
            

        