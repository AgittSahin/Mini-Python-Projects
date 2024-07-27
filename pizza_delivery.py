print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
else:
    bill += 0
    
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 0
    
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 0
    
if extra_cheese == "Y":
    bill += 1
else:
    bill += 0
    
print(f"Your final bill is: ${bill}.")