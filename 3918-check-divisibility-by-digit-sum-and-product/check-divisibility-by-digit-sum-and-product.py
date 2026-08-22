class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        n1 = n
        prod = 1
        while n1 > 0:
            rem = n1 % 10
            s += rem
            prod *= rem
            n1 = n1//10
        tot = s+prod
      
        return True if n % tot == 0 else False 
        