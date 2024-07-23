print("The Love Calculator is calculating your score...")
name1 = input("What is your name ? ") 
name2 = input("What is their name ? ")


def check_name(name):
  true = 0
  love = 0
  for char in name.lower():
    if char == "t":
        true += 1
    elif char == "r":
        true += 1
    elif char == "u":
        true += 1
    elif char == "e":
        true += 1
        love += 1        
    elif char == "l":
        love += 1        
    elif char == "o":
        love += 1        
    elif char == "v":
        love += 1
  return true, love
       
true1, love1 = check_name(name1)
true2, love2 = check_name(name2)

Truee = true1 + true2
Love = love1 + love2
           
love_score = ((Truee * 10) + Love)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")