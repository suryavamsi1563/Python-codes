a = [1, 2, 3, 5, 6, 1, 2, 3, 5, 6]
c = int(input("Enter the number to delete if has second occurence: "))
if a.count(c) >= 2:
    index = a.index(c, (a.index(c)+1))
    a.pop(index)
    print(a)
else:
    print("Given doesnt have a second occurrence")
