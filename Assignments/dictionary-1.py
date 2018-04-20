a = {"net_username": "username1", "net_password": "password1", "net_host": "host1"}
b = {"net.username": "username2", "net.password": "password2", "net.host": "host2"}

a = {x:b[y] for x in a for y in b if x.rsplit('_')[-1] == y.rsplit('.')[-1]}


print(a)
# for x in a.keys():
#     for y in b.keys():
#         if x.rsplit('_')[-1] == y.rsplit('.')[-1]:
#             a[x] = b[y]
# print(a)
