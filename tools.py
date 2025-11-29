import datetime

now = datetime.date.today()
current_year = now.year

def get_age(birth_year):
    age = current_year - birth_year
    return age
def creat_company_email(First_name, Last_name):
    email = First_name + "." + Last_name + "@company.com"
    return email.lower()