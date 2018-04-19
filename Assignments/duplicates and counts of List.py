a = [1,2,3,4,1,1,5,2,3,1,3,2]
b = list(set(a))
print([x for x in b if a.count(x) == 1])
# print([(x,a.count(x)) for x in b if a.count(x)>1])
c = [str(x)+" "+str(a.count(x)) for x in b if a.count(x)>1]
for x in c:
    print(x)
print([str(x)+" repeating "+str(a.count(x))+" times" for x in b if a.count(x)>1])

