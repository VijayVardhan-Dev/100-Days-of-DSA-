Date: 23/05/2026
#today leetcode problem is done with both brute force and efficient way

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count = count+1
        if count <= 1:
            return True
        else:
            return False

