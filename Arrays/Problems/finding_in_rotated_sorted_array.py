Date: 22/05/2026
# today i learned about rotated sorted array and completed daily challnge on leetcode 

arr1 = [4,5,6,7,8,9,10,1,2,3]
target = int(input("Enter number to find: "))
left = 0
right = len(arr1)-1
while left <= right:
    mid = (left + right)//2
    if target == arr1[mid]:
        print(mid)
        break
    else:
        if arr1[left] <= arr1[mid]:
            if target <= arr1[mid] and target >= arr1[left]:
                right = mid-1
            else:
                left = mid+1 
        else:
            if target >= arr1[mid] and target <= arr1[right]:
                left = mid+1
            else:
                right = mid-1
                
       
