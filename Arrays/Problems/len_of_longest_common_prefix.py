

arr1 = [13,27,45]
arr2 = [21,27,48]



set1 = set()
length = 0

for i in arr1:
    set1.add(i)
    while i > 0:
        r = i//10
        set1.add(r)
        i = i//10
        
for j in arr2:
    while j > 0:
        if j in set1:
            if j > length:
                length = j
            break
        j = j//10

if length == 0:
    print(0)
else:
    print(len(str(length)))

