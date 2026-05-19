

num1 = [6,2,3,4,5]
num2 = [8,3,2,1]
final = set(num2)
num1.sort()
flag = 0
for i in num1:
    if i in final:
        print(i)
        flag = 1
        break
    
if flag == 1:
    return -1
