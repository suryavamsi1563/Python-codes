# Finding the second lowest number
# a = [2, 3, 5, 1]
a = [5, 4, 3, 1, 6]
# a = [1, 2, 3, 4, 5]
c, second_low = 0, 0
for x in range(len(a)):
    if x == 0:
        c = a[x]
        second_low = a[x+1]
    else:
        if c > a[x]:
            second_low = c
            c = a[x]
        else:
            if second_low > a[x]:
                second_low = a[x]
print(second_low)
# -----------------------