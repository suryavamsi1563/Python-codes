a, b = map(int, input('Enter two inputs with a space between them: ').split())
print(a, b)


def gcd_calculator(z):
    gcd = 0
    for x in range(1, z+1):
        print("Inside function", x, a, b)
        if a % x == 0 and b % x == 0:
            print("Inside If loop")
            gcd = x

    print(gcd)


if a > b:
    gcd_calculator(b)
elif b > a:
    gcd_calculator(a)
else:
    print("Both numbers are equal.GCD is itself", a)
