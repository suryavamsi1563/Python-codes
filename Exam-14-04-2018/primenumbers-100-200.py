#printng prime numbers betw 100 to 200

for x in range(100, 201):
    for y in range(2, int(x/2)):
        if not x % y:
            break
    else:
        print(x)
# ----------------------------------------