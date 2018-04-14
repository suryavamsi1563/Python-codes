a = [1, 2, 5, 4, 6, 3, 2, 8, 9, 1, 22, 26]
largest, second_largest, third_largest = 0, 0, 0

for x in range(len(a)):
    if x == 0:
        largest = a[x]
        second_largest = a[x+1]
        third_largest = a[x+2]
    else:
        if a[x] > largest:
            third_largest = second_largest
            second_largest = largest
            largest = a[x]
        else:
            if a[x] > second_largest:
                third_largest = second_largest
                second_largest = a[x]
            else:
                if a[x] > third_largest:
                    third_largest = a[x]
print(third_largest)

print("Largest Number is:", largest)
print("Second largest number is: ", second_largest)
print("Third  largest number is: ", third_largest)



