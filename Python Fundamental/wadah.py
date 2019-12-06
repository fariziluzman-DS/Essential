x = [1,2,3,4,5,6,7,8,9]
y = []
for item in x:
    if ((item not in y) and (item % 2 == 0)):
        y.append(item)
print(y)