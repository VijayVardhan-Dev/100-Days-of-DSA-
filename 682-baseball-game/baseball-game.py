class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stack_sum = 0
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
            
        for i in operations:
            if is_integer(i):
                val = int(i)
                stack.append(val)
                stack_sum += val
            elif i == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)
                stack_sum += val
            elif i == 'C':
                val = stack.pop()
                stack_sum -= val
            else:
                val = stack[-1] * 2
                stack.append(val)
                stack_sum += val
        return stack_sum


        