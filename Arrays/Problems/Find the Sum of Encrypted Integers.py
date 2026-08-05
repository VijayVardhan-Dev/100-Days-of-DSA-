Find the Sum of Encrypted Integers

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        max = 0
        sum = 0
        for i in nums:
            lent = len(str(i))
            while i > 0:
                val = i % 10 
                i = i//10
                if val > max:
                    max = val
            sum = sum + int(str(max)*lent)
            max = 0
        return sum
                

        
