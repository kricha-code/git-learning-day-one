from tools import creat_company_email

# 1. READ the data from a text file
with open("employees.txt", "r") as file:
    employees = file.readlines()
    
# 2. WRITE the processed data to a new CSV file
with open("employees_emails.csv", "w") as file:

    # A. Write the Column Headers for Excel
    file.write("Name,Email\n")

    # B. The Factory Loop
    for name in employees:

        # Clean the name (remove the invisible \n from the text file)
        clean_name = name.strip()

        # Unpack the first and last name
        first,last = clean_name.split(" ")

        # Generate Email using your tool
        email = creat_company_email(first, last)

        # Write to file: "Name,Email" and add a New Line (\n) at the end
        file.write(f"{clean_name},{email}\n")

    print(f"Processing : {clean_name}")