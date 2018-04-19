a = input("Enter the numbers with a space: ")
print(a)
b = 0
c = []
for x in range(len(a)):
    if a[x] ==' ':
        c.append(a[b:x])
        b = x+1
c.append(a[b:])
print(c)
