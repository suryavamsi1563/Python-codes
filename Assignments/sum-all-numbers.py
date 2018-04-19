# print([int(x)+ int(y) for x,y in zip(input("Enter the variables with space of 1st : ").split(),
#                           input("Enter the variables with spaceof 2nd : ").split())])
# a = input("Enter the variables with space of 1st : ").split()
# b = input("Enter the variables with space of 2nd : ").split()
# print([int(x)+ int(y) for x in a
#                        for y in b if a.index(x) == b.index(y)])

# print([int(x)+ int(y) for x in input("Enter the variables with space of 1st : ").split()
#                        for y in input("Enter the variables with space of 2nd : ").split()])
#
# print(a)
# b = [10,20,30,40]
# print(sum(b))
print(sum([int(x) for x in input("Enter the variables with space: ").split()]))
