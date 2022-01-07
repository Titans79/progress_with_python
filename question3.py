# -> INPUT
payrol_No = input("Payrol No: ")

def employee_grade():
    entered = input("Grade (X/Y): ").upper()

    while (entered != "X") and (entered != "Y"):
        print("(hint: grade must be X or Y ...)")
        entered = input("Enter grade: ")

    return entered

grade = employee_grade()
hrs_worked = int(input("Hours Worked: "))
distance_travelled = int(input("Distance travelled: "))

# GROSS PAY
def gross_pay():

    # wage_rate
    wage_rate = 0

    if grade == "X":
        wage_rate = 1100
    else:
        wage_rate = 1300

    # 1. basic pay
    basic_pay = hrs_worked * wage_rate

    # 2. mileage
    mileage = 0

    if grade == "X":
        mileage = 50 * distance_travelled
    elif grade == "Y":
        mileage = 90 * distance_travelled
        if mileage > 50000:
            mileage = 50000


    # 3. house_allowance
    house_allowance = 0
    if grade == "X":
        house_allowance = 15000


    return basic_pay + mileage + house_allowance


# TAX
tax = 0

if gross_pay() > 33000:
    tax = .1 * gross_pay()

# NET PAY
net_pay = gross_pay() - tax


# OUTPUT ->

print(("*")*40)
print(f" Payroll Number => { payrol_No }")
print(f" Gross Pay => { gross_pay() }")
print(f" Net Pay => { net_pay }")
print(("*")*40)


