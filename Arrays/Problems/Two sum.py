
date: 17/05/2007

#two sum program to print all unique pairs with O(n^2)

n = int(input("Enter your Target: "))
list1 = [2,7,3,6,7]
list2 = []
final = []
for i in list1:
    if abs(n-i) in list1:
        list2.append([i,n-i])


for i in list2:
    sorted_list = sorted(i)
    if sorted_list not in final:
        final.append(sorted_list)

print(final)



#two sum program to print all unique pairs with O(n)
#here we used set to get unique elements only

n = int(input("Enter your Target: "))
list1 = [2,7,3,6,7]
processed = set()
final = set()
for i in list1:
    if n-i in processed:
        final.add(tuple(sorted([n-i,i])))  #to add into set need to convert list into tuple
    processed.add(i)

print(list(final))
