a = "switch_name: switch1 \n username: username1 \n password: password1 \n host: host1 router: router1"
b = a.split()
print(b)
for x in b:
    if x.startswith('user') or x.startswith('pass') or x.startswith('host'):
        print(x)
        b.remove(x)
c = ' '.join(b)
print(c)
