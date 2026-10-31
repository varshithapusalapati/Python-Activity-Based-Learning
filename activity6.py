name = input("Enter patient name: ")

c = int(input("Consultation charge: "))
d = int(input("Diagnostic charge: "))
t = int(input("Treatment charge: "))

total = c + d + t

if total >= 5000:
    discount = total * 10 / 100
else:
    discount = 0

final = total - discount

print("Patient Name:", name)
print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final)

if final >= 5000:
    print("Premium Patient")
else:
    print("Regular Patient")