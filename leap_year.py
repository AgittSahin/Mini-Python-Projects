def leap_year(year):
    if year % 4 != 0:
        return print(f"{year} is not a leap year.")
    elif year % 4 == 0 and year % 100 != 0:
        return print(f"{year} is a leap year.")
    elif year % 4 == 0 and year % 100 == 0:
        if year % 400 != 0:
            return print(f"{year} is not a leap year.")
        else:
            return print(f"{year} is a leap year.")
        
leap_year(int(input("What is the year you want to check: ")))
        
