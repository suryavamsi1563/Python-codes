a = [r'C:\python\introduction.py',r'C:\python\datatypes\int.py',r'C:\python\sequences\list.txt']
# print([y for x in a for y in x.rsplit('\\') if y.endswith(".py")])
#
# print([x[0:x.rfind('\\')] for x in a])
# print([x.rsplit('\\',1) for x in a] )

print([x.rsplit('\\',1)[1] for x in a if x.rsplit('\\',1)[-1].endswith(".py")])