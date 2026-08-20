class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        i = 2
        j = 0
        while j < 2:
                if j%2 == 0:
                    arr1.append(nums[j])
                else:
                    arr2.append(nums[j])
                j+=1
       
        while i < len(nums):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            i += 1
                
        return arr1+arr2
        