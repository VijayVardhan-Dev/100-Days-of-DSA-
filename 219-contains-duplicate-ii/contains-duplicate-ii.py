class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        window = set()
        for r in range(N):
            if r > k:
                window.remove(nums[r-k-1])

            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
            

        