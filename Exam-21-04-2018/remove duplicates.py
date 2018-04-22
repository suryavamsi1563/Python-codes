a = [1,2,3,5,1,3,4,2,6,4,2,1,2,5,6]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)