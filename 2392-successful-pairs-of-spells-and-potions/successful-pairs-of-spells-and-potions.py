class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()
        final = []
        for i in spells:
            l = 0
            r = n
            while l < r:
                mid = (l+r)//2
                if potions[mid] * i >= success:
                    r = mid
                else:
                    l = mid+1
                
            final.append(n-l)
        return final
            
        