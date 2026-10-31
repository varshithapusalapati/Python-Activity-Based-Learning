orders = [10, 20, 15]
dispatched = [8, 20, 10]
returned = [2, 0, 3]

for i in range(3):
    if dispatched[i] > orders[i] or returned[i] > dispatched[i]:
        print("Invalid Record")
    else:
        outstanding = orders[i] - dispatched[i]
        stock = returned[i]

        print("Order:", orders[i])
        print("Outstanding:", outstanding)
        print("Returned:", stock)