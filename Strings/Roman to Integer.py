class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        i = 0
        while i < (len(s)):
            if i <= len(s)-2:
                if val[s[i]] >= val[s[i+1]]:
                    sum += val[s[i]]
                else: 
                    sum += val[s[i+1]] - val[s[i]]
                    i += 1
            else:
                sum += val[s[i]]
            i += 1
        return sum        
