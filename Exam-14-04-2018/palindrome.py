def reverse_number(a):
    num, reverse = a, 0
    x = 1
    while x == 1:
        reverse = num % 10 + (reverse * 10)
        num = int(num / 10)
        # num = a % 10  gives the right most digit
        # num = num/10 # gives the remaining left most digits
        print(reverse)
        if num == 0:
            return reverse


a = int(input("Enter the number: "))
reverse_of_a = reverse_number(a)
if reverse_of_a == a:
    print("The number is Palindrome")
else:
    print(print("not a palindrome"))

# Using string functionality in python

b = 1225
c = str(b)[::-1]
if b == int(c):
    print("The number is palindrome")
else:
    print("The number is not a palindrome")
