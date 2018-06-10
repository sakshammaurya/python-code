#python3
n, weight = map(int,input().split())

costWeight = []
for i in range(n):
    c, w = map(int, input().split())
    costWeight.append((c, w, c * 1.0 / w))

sortedWeight = sorted(costWeight, key=lambda x:x[2], reverse=True)
totalCost = 0
for tup in sortedWeight:
    if weight >= tup[1]:
        weight = weight-tup[1]
        totalCost= tup[0]+totalCost
    else:
        totalCost = weight * 1.0 / tup[1] * tup[0]+totalCost
        break

print(totalCost)






































































































































