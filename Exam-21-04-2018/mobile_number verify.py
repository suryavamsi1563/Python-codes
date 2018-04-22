a = "My mobile number is +91-8148586079"
mobile_number = a.split()[-1]
Inter_code, phone_number = mobile_number[:2], mobile_number[4:]
print(Inter_code)
print(mobile_number)
if Inter_code == '+91' and len(phone_number) != 10:
    print(" The number entered is a valid indian mobile number")
else:
    print("The mobile number is not indian mobile number")
