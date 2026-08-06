class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max = 0
        while l < r:
            val = (r-l)*min(height[l],height[r])
            if max < val:
                max = val
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1
        return max      
