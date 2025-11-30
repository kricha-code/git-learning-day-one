from tools import creat_company_email

employees = [ "Mike Saul" , "Jamie MCguile" , "Walter Black"]
for individual_name in employees:
    print(individual_name)
    names = individual_name.split(" ")
    print("company email: " + creat_company_email(names[0], names[1]))