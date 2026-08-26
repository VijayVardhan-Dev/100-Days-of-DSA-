class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        count = 0
        
        answer = ""
        l = 0
        r = 0 
        N = len(s)
        min_l = N+1
        while r < N:
            #for creating valid substring
            while r < N and count != k:
                if s[r] == '1':
                    count += 1
                r += 1
            # for choosing valid minimum lexicographically beautiful substring
            if count == k:

                while l < r and s[l] == '0':
                    l += 1

                cur = s[l:r]

                if r-l < min_l:
                    answer = cur
                    min_l = r-l
                    
                elif r-l == min_l:
                    if answer > cur:
                        answer = cur  
      
            if l<r and count == k:
                if s[l] == '1':
                    count -= 1
                l+=1

        return answer

                


        