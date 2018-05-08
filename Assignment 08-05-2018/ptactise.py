class MyInt:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return self.value * other.value


x = MyInt(25)
y = MyInt(2)
z = 56
print(x)
print(y)
print(x+y+z)



