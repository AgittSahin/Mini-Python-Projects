import random

#random_integer = random.randint(1,10)
#random_floating = int(random.random() * 10)

####################################################################
entries = input()
names = entries.split(", ")
lucky_person = random.randint(0,len(names)-1)
print(f"{names[lucky_person]} is going to buy the meal today!")


