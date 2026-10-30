products = [
    (101, 100, 10),
    (102, 200, 0),
    (103, -50, 5),
    (104, 150, 2)
]

for p in products:
    if p[1] < 0 or p[2] < 0:
        print(p[0], "Invalid Record")
    else:
        print("Product:", p[0])
        print("Inventory Value:", p[1] * p[2])

        if p[2] < 5:
            print("Replenishment Required")
