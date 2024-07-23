print("Welcome to the tip calculator!")

total_bill = int(input("What was the total bill? "))
tip_percent = int(input("How much would you like to give ? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
result = total_bill * (tip_percent / 100) / people

print(f"Each person should pay: ${result}")