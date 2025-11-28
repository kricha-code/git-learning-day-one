Name = input("Name")

try:
    Age = 2025- int(input("Birth Year"))

    print(f"Your name is {Name} and you are {Age} years old.")
    if Age < 18:
        print("You are a minor. Please get parent permission.")
    elif Age < 65:
        print("Welcome to the team!")
    else:
        print("You are eligible for the senior pension plan!")
except:
    print("Oh no! Please type number (like 1999), not words.")