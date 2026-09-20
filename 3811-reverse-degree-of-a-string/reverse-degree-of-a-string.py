class Solution:
    def reverseDegree(self, s: str) -> int:
        summ = 0
        for i in range(len(s)):
            summ += (27 - (ord(s[i].upper()) - ord('A') + 1)) * (i + 1)
        return summ
        