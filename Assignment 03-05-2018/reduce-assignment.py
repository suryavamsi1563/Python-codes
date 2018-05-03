from functools import reduce

a = {'host1': ['network1', 'network2', 'network3'],
     'host2': ['network5', 'network2', 'network1', 'network10'],
     'host3': ['network1', 'network15', 'network13', 'network5']}
# for x in a:
#     print(set(a[x]))

# print(list(a.values()))

print(reduce(lambda x, y: list(set(x).intersection(set(y))), list(a.values())))



