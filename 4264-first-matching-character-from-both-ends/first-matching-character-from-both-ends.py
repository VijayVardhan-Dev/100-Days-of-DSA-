class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        N = len(s)
        l = 0
        r = N-1
        while l <= r:
            if s[l] == s[r]:
                return l
            l += 1
            r -= 1
        return -1
        