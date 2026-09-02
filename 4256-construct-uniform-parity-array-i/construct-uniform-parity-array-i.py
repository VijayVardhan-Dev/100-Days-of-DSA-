class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        N = len(nums1)
        i = 0
        flag = 0
        for j in range(i + 1 , N):
            one = nums1[i] % 2 == 0
            two = (nums1[i] - nums1[j]) % 2 == 0
            if flag == 1 and (not one and not two):
                return False
            if flag == -1 and (one and two):
                return False
            if one and two:
                flag = 1
            elif not one and not two:
                print("hi")
                flag = -1
        return True
        