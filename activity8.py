usage = int(input("Enter data usage in GB: "))
budget = int(input("Enter your budget: "))

if usage <= 50:
    cost = 100
    plan = "Basic"
elif usage <= 100:
    cost = 200
    plan = "Standard"
else:
    cost = 300
    plan = "Premium"

if cost <= budget:
    print("Selected Plan:", plan)
    print("Plan Cost:", cost)
else:
    print("Plan is not available within budget")