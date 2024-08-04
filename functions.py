def greet(name):
    print(f"Hello, {name}")
    print("It is nice to see you !")
    print("How are you ?")
    
greet("George")

# name is the "Parameter" George is the "Argument"

#function with more than 1 input
def greet_with(name, location):
    print(f"My name is, {name}")
    print(f"I am from {location}")
    
#Positional Arguments
greet_with("Agit", "Switzerland")
#Keyword Arguments
greet_with(location = "Switzerland", name = "Agit")


