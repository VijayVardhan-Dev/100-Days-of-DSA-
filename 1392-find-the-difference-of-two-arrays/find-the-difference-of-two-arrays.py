class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1s = set(nums1)
        num2s = set(nums2)
        final = []
        final.append(list(num1s - num2s))
        final.append(list(num2s - num1s))
        return final

        