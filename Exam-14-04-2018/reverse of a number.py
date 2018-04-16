a = 10256489
a_string = str(a)
a_list = list(a_string)
a_list.reverse()
b = ''
for x in a_list:
    b = b + x
print(int(b))
