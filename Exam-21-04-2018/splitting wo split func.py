a = "this is a python class"
b = []
c = 0
for x in range(len(a)):
    if a[x] == " ":
        b.append(a[c:x])
        c = x+1
b.append(a[c:])
print(b)

