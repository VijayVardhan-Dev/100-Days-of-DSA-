class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N = len(s1)
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        l = 0

        if N > len(s2):
            return False

        for i in s1:
            s1_freq[i] += 1

        for i in range(N):
            s2_freq[s2[i]] += 1

        if s1_freq == s2_freq:
                return True

        for i in range(N,len(s2)):
        
            s2_freq[s2[i]] += 1
            s2_freq[s2[l]] -= 1

            if s2_freq[s2[l]] == 0:
                s2_freq.pop(s2[l])
            
            if s1_freq == s2_freq:
                return True

            l += 1

        return False




        