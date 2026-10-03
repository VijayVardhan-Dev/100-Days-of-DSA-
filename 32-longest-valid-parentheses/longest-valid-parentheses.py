class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            if stack and s[i] == ")" and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)
            
        index = -1
        max_c = 0
        for i in stack:
            max_c = max(max_c , i - index - 1)
            index = i
        
        max_c = max(max_c , len(s) - index - 1)

        return max_c

                
            
