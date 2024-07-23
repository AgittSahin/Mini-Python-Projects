print("Welcome to the RollerCoaster!!!")
height = int(input("What is your height in cm ? "))
bill = 0

if height >= 120:
    print("Congrats you can ride!")
    age = int(input("What is your age ? "))
    
    if age < 12:
        bill += 5
    elif age >= 18 and age < 45:
        bill += 12
    elif age >= 45 and age <= 55:
        bill += 0
    else:
        bill += 7
        
    photo = input("Do you want a picture? y/n ")
    
    if photo == "y":
        bill += 3
    elif photo == "n":
        bill += 0
        
    print(f"Your final bill is ${bill}") 
else:
    print("Sorry, you need to grow before you can ride.")