from tools import creat_company_email

employees = [ "Mike Saul" , "Jamie MCguile" , "Walter Black"]
for individual_name in employees:
    print(individual_name)
    first_name, last_name = individual_name.split(" ")
    print("company email: " + creat_company_email(first_name, last_name))
    print("-"*40)