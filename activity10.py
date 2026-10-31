total = 0

n = int(input("Enter number of violations: "))

for i in range(n):
    vehicle = input("Enter vehicle type: ")
    offence = input("Enter offence (helmet/signal): ")
    repeat = input("Repeat offence (yes/no): ")

    if offence == "helmet":
        fine = 500
    elif offence == "signal":
        fine = 1000
    else:
        fine = 0

    if repeat == "yes":
        fine = fine * 2

    if vehicle == "heavy" and offence == "signal":
        print("Vehicle disqualified")
    else:
        print("Fine:", fine)

    total = total + fine

print("Total Penalty:", total)

