height = float(input())
weight = int(input())

bmi = weight / (height ** 2)
bmi = float(bmi)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")