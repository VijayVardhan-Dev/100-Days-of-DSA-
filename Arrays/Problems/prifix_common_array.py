#Date: 20/05/2026
# Today i was able to solve medium level problem on leetcode even tough it is bruteforce approach but i will improve it...

A = [1,3,2,4]
B = [3,1,2,4]
C = []
count = 0
for i,num in enumerate(A):
    count = 0
  
    for j in range(i+1):
        found = False
        for k in range(i+1):
            if B[j] == A[k]:
                found = True
                break
        if found:
            count = count+1  
    C.append(count)
print(C)
