import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

commands = {
    0 : rock,
    1 : paper,
    2 : scissors
}

computer_desicion = commands.get(random.randint(0,2))
user_desicion = commands.get(int(input("What is your choice rock: 0 paper: 1 scissors: 2: ")))

print(user_desicion)
print(computer_desicion)

if user_desicion == rock and computer_desicion == scissors:
    print("YOU WIN!!!")
elif user_desicion == paper and computer_desicion == rock:
    print("YOU WIN!!!")
elif user_desicion == scissors and computer_desicion == paper:
    print("YOU WIN!!!")
elif user_desicion == computer_desicion:
    print("DRAW")
else:
    print("You Lost :(")
    