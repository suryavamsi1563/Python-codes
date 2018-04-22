a = "we have completed 12 classes for python and remaining classes are 25." \
    "Till now we have covered 30 topics and remaining are 50 topics"

# Finding total number of digits,spaces in above string
digits_count = 0
digits_space = 0
c = []
digits_unique = 0
for x in a:
    if x.isdigit():
        digits_count += 1
        if x not in c:
            c.append(x)
            digits_unique += 1
    elif x.isspace():
        digits_space += 1
print(digits_count)
print(digits_space)
print(digits_unique)
