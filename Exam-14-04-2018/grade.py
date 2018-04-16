marks = []
for x in range(5):
    marks.append(int(input('Enter the marks in subject :')))

print(marks)
avg = sum(marks)//5
if avg > 90:
    grade = 'A'
elif avg <= 90 and avg >80:
    grade = 'B'
else:
    grade = 'C'
print(grade)
