# input is comma separated and get the sum of the elements without using list comprehension
# or lambda

# print(sum(list(map(int, input("Enter inputs with comma separation: ").split(',')))))

# take two inputs one with space separation and second with comma separation.add both elements wise
# and convert the result into sum values separated by @
a = list(map(int,input("Enter inputs with comma separation: ").split(',')))
print(a)


b = list(map(int,input("Enter inputs with space separation: ").split()))
print(b)
#
# print('@'.join(list(map(lambda x, y: (str(int(x)+int(y))), a, b))))

print('@'.join(list(map(str(zip(a, b))))))

# print('@'.join([x+y for x, y in zip(a, b)]))
