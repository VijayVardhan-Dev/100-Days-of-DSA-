class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        n = len(s)
        freq = {}
        for i in range(len(s)):
           freq[s[i]] = freq.get(s[i],0)+1
        s = set(freq.values())
        if len(s) == 1:
            return True
        else:
            return False 
        


        