



days = int(input("Enter no of day's: "))
dayList = []
sum = 0
count = 0
for i in range(1,days+1):
    value = int(input(f"Enter day{i} temperature: "))
    dayList.append(value)

len = len(dayList)

for i in dayList:
    sum = sum + i

avg = sum/len

print(avg)

for i in dayList:
    if i > avg:
        count = count + 1

print(count)
        
