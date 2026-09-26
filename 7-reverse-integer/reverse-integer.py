class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x < 0 else 0
        x = abs(x)
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        if sign == 1:
            rev *= -1
        if rev < -2 ** 31 or rev > 2 ** 31:
            return 0
        return rev
