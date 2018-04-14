a = [1, 5, 6, 9, 8, 7, 4, 2, 3]
largest = 0
for x in a:
    if a.index(x) == 0:
        largest = x
    else:
        if x > largest:
            largest = x
print("Largest Number is:", largest)
