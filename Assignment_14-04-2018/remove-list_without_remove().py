a = [1, 2, 5, 4, 6, 3, 2, 8, 9, 1, 22, 26]
print(a)
value = int(input("Enter the value to be removed from the list: "))
a.pop(a.index(value))
print(a)
