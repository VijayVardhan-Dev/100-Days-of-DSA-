#Date 1/06/2026
#competed leetcode daily challange
costs = [6,5,7,9]
costs.sort(reverse = True)
cost = 0
n = len(costs)
for i in range(n):
   if i % 3 != 2:
       cost = cost + costs[i]
print(cost)
