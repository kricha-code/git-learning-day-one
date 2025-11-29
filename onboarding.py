from tools import get_age
from tools import creat_company_email

First_name = input("First Name")
Last_name = input("Last Name")
Name = First_name + " " + Last_name

try:
    Age = get_age(int(input("Birth year")))

    print(f"Your name is {Name} and you are {Age} years old.")
    if Age < 18:
        print("You are a minor. Please get parent permission.")
    elif Age < 65:
        print("Welcome to the team!")
    else:
        print("You are eligible for the senior pension plan!")
except:
    print("Oh no! Please type number (like 1999), not words.")

print("Your company email is: " + creat_company_email(First_name, Last_name))