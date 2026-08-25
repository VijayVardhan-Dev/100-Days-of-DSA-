class Solution:
    def reverseByType(self, s: str) -> str:
        N = len(s)
        s = list(s)
        l = 0
        r = N-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        l = 0
        r = N-1
        while l < r:
            while l < r and  s[l].isalnum():
                l += 1
            while l < r and  s[r].isalnum():
                r -= 1
            if l < r:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        return "".join(s)
        