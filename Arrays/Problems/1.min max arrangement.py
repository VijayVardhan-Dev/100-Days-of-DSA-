"""
Problem: Given a sorted array A of size n, rearrange it in-place into: max, min, 2nd max, 2nd min, .... Do it in O(n) time and O(1) extra space.
Difficulty: Easy
Topic: Arrays
Date: 2025-10-17
Approach:
1. Two pointer on array.
Use two pointers:
left = 0 (smallest)
right = n-1 (largest)

2. O(n log n) time, O(n) space.

"""

arr = [1, 2, 3, 4, 5]
arr.sort()
sorted_array = []
left,right = 0,len(arr)-1
while left <= right:
    if left != right:
        sorted_array.append(arr[right])
        sorted_array.append(arr[left])
    else:
        sorted_array.append(arr[left])    
    
    left+=1
    right-=1    
print(sorted_array)
