class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ob = {'(','[','{'}
        for i in s:
            if i in ob:
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True

        
        