class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stack_sum = 0
            
        for i in operations:
            if i == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)
                stack_sum += val
            elif i == 'C':
                val = stack.pop()
                stack_sum -= val
            elif i == 'D':
                val = stack[-1] * 2
                stack.append(val)
                stack_sum += val
            else:
                val = int(i)
                stack.append(val)
                stack_sum += val

        return stack_sum


        