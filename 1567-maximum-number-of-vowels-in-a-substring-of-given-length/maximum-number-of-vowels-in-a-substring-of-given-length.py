class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l  = 0
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_c = count
        for i in range(k,len(s)):
            if s[i] in vowels:
                count += 1
            if s[l] in vowels:
                count -= 1
            if count > max_c:
                max_c = count
            l += 1
        return max_c

 