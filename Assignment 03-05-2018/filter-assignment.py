# read numbers from console and print prime numbers from the inputnumbers by using only  a function and a single line


def prime_or_not(x):

        if int(x) == 2:
            return True
        for i in range(2, int(int(x)/2 + 1)):
            if int(x) % i == 0:
                return False
        else:
            return True


print(list(filter(prime_or_not, input('Enter the numbers space separated: ').split())))

