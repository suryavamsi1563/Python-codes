def GetType():
    prompt = input('Enter the input as "H" or "C" or "S" :').upper()
    while prompt not in ("H", "C", "S"):
        prompt = input('Please enter a value from "H" or "C" or "S" :').upper()
    return prompt


def GetNumOfWorkHours():
    work_hours = int(input("Enter Your Work Hours: "))
    while work_hours <= 0:
        work_hours = int(input("Work Hours must be greater than ZERO.Please Re-enter :"))
    return work_hours


def GetTargetWeeklyWorkHours():
    target_work_hours = int(input("Enter Your Target Weekly Work Hours: "))
    while target_work_hours not in (20, 32, 40):
        target_work_hours = int(input("Target Weekly Work Hours must be 20 or 32 or 40: "))
    return target_work_hours


def GetHourlywage():
    hourly_wages = int(input("Enter the hourly wages: "))
    while hourly_wages not in (10, 15, 24):
        hourly_wages = int(input("Hourly wage must be 10 or 15 or 24.Please Ree-enter: "))
    return hourly_wages


def CalcExtraBonus(work_hours):
    Extra_Bonus = 0
    Target_work_hours = GetTargetWeeklyWorkHours()
    print('Target work hours are :', Target_work_hours)
    hours_of_bonus = work_hours - Target_work_hours
    print('Hours of Bonus are: ', hours_of_bonus)
    if hours_of_bonus <=0:
        Extra_Bonus = 0
    elif Target_work_hours == 20:
        Extra_Bonus = 12
    elif Target_work_hours == 32:
        Extra_Bonus = 18
    elif Target_work_hours == 40:
        Extra_Bonus = 24
    else:
        print("Target_work_hours are entered incorrectly.Please re-enter.")
    print("Extra Bonus for Hour is: ",Extra_Bonus)
    total_bonus = hours_of_bonus * Extra_Bonus
    return total_bonus


def HourlySalary():
    work_hours = GetNumOfWorkHours()
    print('Work Hours are : ', work_hours)
    hourly_wage = GetHourlywage()
    print('Hourly wage is: ', hourly_wage)
    extra_bonus = CalcExtraBonus(work_hours)
    print('Extra Bonus is: ', extra_bonus)

    total_salary = (work_hours * hourly_wage) + extra_bonus
    return total_salary

# Functions for monthly contract employees
def getnumofdays(x):
    num_of_days = int(input(x))
    while num_of_days < 0:
        num_of_days = int(input("Number of days must be greater than zero.Please re-enter"))
    return num_of_days


def getbasicsalary():
    basicsalary = int(input("Enter your basic  salary: "))
    while basicsalary not in (3000, 4000, 5000):
        basicsalary = int(input("Basic salary must be 3000 or 4000 or 5000.Please re-enter: "))
    return basicsalary


def calcextrabonus(basic_salary):
    days_of_bonus = getnumofdays('How many days you worked in public holidays or rest holidays: ')
    extra_bonus = 0
    if days_of_bonus == 0:
        extra_bonus = 0
    elif basic_salary == 3000:
        extra_bonus = 270
    elif basic_salary == 4000:
        extra_bonus = 360
    elif basic_salary == 5000:
        extra_bonus = 450
    else:
        print("Entered basic salary is incorrect.")
    total_extra_bonus = days_of_bonus * extra_bonus
    return total_extra_bonus


def calcdeductiblewage(basic_salary):
    absent_days = getnumofdays('Enter how many days your are absent: ')
    deductible_wage = 0
    if absent_days == 0:
        return 0
    elif basic_salary == 3000:
        deductible_wage = 135
    elif basic_salary == 4000:
        deductible_wage = 180
    elif basic_salary == 5000:
        deductible_wage = 225
    return absent_days * deductible_wage


def calcfullattendancebonus(basic_salary):
    work_of_days = getnumofdays('How many days employee worked: ')
    full_attendance_bonus = 0
    if work_of_days < 22:
        full_attendance_bonus = 0
    elif basic_salary == 3000 and work_of_days >=22:
        full_attendance_bonus = 300
    elif basic_salary == 4000 and work_of_days>=22:
        full_attendance_bonus = 400
    elif basic_salary == 5000 and work_of_days>= 22:
        full_attendance_bonus = 500
    return full_attendance_bonus


def total_salary_monthly():
    basic_salary = getbasicsalary()
    print("Basic Salary entered is : ", basic_salary)
    extra_bonus = calcextrabonus(basic_salary)
    print("Extra bonus is", extra_bonus, sep=': ')
    total_deductible_wage = calcdeductiblewage(basic_salary)
    print("Deductions in wage are: ", total_deductible_wage)
    full_attendance_bonus = calcfullattendancebonus(basic_salary)
    print("Full attendance bonus is  :", full_attendance_bonus)
    return basic_salary+extra_bonus+full_attendance_bonus - total_deductible_wage


type_of_employee = GetType()
if type_of_employee == 'H':
    salary = HourlySalary()
    print("Salary Calculate", salary, sep=': ')
elif type_of_employee == 'C':
    salary = total_salary_monthly()
    print("salary calculated is :",salary,sep=': ')
