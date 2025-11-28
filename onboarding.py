Name = input("Name")

try:
    Age = 2025- int(input("Birth Year"))

    print(f"Your name is {Name} and you are {Age} years old.")
except:
    print("Oh no! Please type number (like 1999), not words.")