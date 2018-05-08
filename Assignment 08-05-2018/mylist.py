# class MyList(list):
#     def __init__(self, list1):
#         self.list = list1
#
#     def __str__(self):
#         return str(self.list)
#
#     def __add__(self, other):
#         return self.list * other
#
#
# x = MyList([1, 2, 3, 5, 6])
# print(x)
# print(x+3)
#

# birthdays = {'Alice': 'Mar 4', 'Su': 'April 9', 'Surya': 'Oct10'}
# print(list(birthdays.keys()))
# print(birthdays.values())
# print(birthdays.items())
#
# for x in birthdays.items():
#     print(x)
from pprint import pprint as p1

message = "I want to  be good"
count = {}
for i in message:
    count.setdefault(i, 0)
    count[i] += 1
p1(count)
# y = pprint.pformat(count)
# print(y)