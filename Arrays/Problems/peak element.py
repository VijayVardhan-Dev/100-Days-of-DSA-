#date: 19/05/2007
#Brute force solution o(n)

nums = [1,2,3,2,1]

for i,num in enumerate(nums):
    left = float('-inf') if i == 0 else nums[i-1]
    right = float('-inf') if i == len(nums)-1 else nums[i+1]
    if num > left and num > right:
        print(num,i)
        break
  
# to be continued to solve with o(logn) solution
