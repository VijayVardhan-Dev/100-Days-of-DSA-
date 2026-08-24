class Solution:

    def reverseByType(self, s: str) -> str:

        s = list(s)

        N = len(s)

        l = 0
        r = N - 1

        while l < r:

            if s[l].isalpha():

                while r > l and not s[r].isalpha():
                    r -= 1

                if l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1

            else:
                while l < r and not s[l].isalpha():
                    l += 1

        l = 0
        r = N - 1

        while l < r:

            if not s[l].isalnum():

                while r > l and s[r].isalnum():
                    r -= 1

                if l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1

            else:
                l += 1

        return "".join(s)