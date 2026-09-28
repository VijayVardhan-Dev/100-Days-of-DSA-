class Solution:
    def maxDepth(self, s: str) -> int:
        maxc = 0
        c = 0
        for ch in s:
            if ch == '(':
                c += 1
            if ch == ')':
                c -= 1
            maxc = max(c,maxc)
        return maxc


        