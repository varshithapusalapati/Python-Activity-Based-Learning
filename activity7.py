name = input("Enter employee name: ")

basic = int(input("Enter basic salary: "))
allowance = int(input("Enter allowance: "))
overtime = int(input("Enter overtime: "))
incentive = int(input("Enter incentive: "))

gross = basic + allowance + overtime + incentive

if gross <= 10000:
    deduction = gross * 5 / 100
elif gross <= 20000:
    deduction = gross * 10 / 100
else:
    deduction = gross * 15 / 100

net = gross - deduction

print("Employee Name:", name)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)