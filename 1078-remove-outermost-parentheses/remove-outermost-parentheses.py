class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        i = 0
        while i < len(s):
            if i == 0:
                s[i]=" "
            elif s[i] == "(":
                stack.append("(")
            elif s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    s[i] = " "
                    i += 1
                    if i < len(s):
                        s[i] = " "
            i += 1
        s = "".join(s)
        return "".join(s.split(" "))
                

            
        