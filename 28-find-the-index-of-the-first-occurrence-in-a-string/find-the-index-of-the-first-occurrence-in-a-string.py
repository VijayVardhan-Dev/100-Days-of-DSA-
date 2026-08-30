class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle = list(needle)
        l = 0
        N = len(needle)
        curstr = []
        if N > len(haystack):
            return -1
        for i in range(N):
            curstr.append(haystack[i])
        if curstr == needle:
            return 0
        for i in range(N,len(haystack)):
            curstr.append(haystack[i])
            curstr.remove(haystack[l])
            l += 1
            if curstr == needle:
                return i+1-N
        return -1

            

    