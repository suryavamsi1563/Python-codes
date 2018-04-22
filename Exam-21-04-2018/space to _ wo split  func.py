a = "this is a python class"
# without using split function as below
n = a.replace(' ', '_')
# by using join and split
b = '_'.join(a.split())
print(b)
print(n)
