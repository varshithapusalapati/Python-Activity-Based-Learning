days = int(input("Enter number of days: "))
start = int(input("Enter starting day (0-6): "))

print("Mon Tue Wed Thu Fri Sat Sun")

for i in range(start):
    print("    ", end="")

for i in range(1, days + 1):
    print("%3d" % i, end=" ")

    if (i + start) % 7 == 0:
        print()

print()
