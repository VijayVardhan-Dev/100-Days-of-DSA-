class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = {'+','-','*','/'}
        for i in tokens:
            if i in operand:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '-':
                    stack.append(b-a)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(i))
                
        return stack[-1]

        