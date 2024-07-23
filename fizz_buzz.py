number = int(input())

for check in range(1,number+1):
    if (check % 3 == 0) and (check % 5 == 0):
        print("FizzBuzz")
    elif check % 5 == 0:
        print("Buzz")
    elif check % 3 == 0:
        print("Fizz")
    else:
        print(check)