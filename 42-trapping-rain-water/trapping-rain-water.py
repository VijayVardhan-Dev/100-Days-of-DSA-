class Solution:
    def trap(self, height: list[int]) -> int:
        left_max = []
        right_max = []

        lmax = 0
        rmax = 0
        
        for i in range(len(height)):

            lmax = max(lmax , height[i])
            left_max.append(lmax)
            
        for i in range(len(height)-1,-1,-1):

            rmax = max(rmax , height[i])
            right_max.append(rmax)
            
        right_max.reverse()
        sum = 0

        for i in range(len(height)):
            sum += min(left_max[i] , right_max[i]) - height[i]

        return sum

        