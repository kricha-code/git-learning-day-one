with open("employees.txt", "r") as file:
    # 2. Read lines into a LIST
    employees = file.readlines()
    
# 3. Prove it is a list    
print(employees)

# 4. Loop through it (The Conveyor Belt)
for name in employees:
    # 5. Clean the name (Remove the invisible "Enter" character \n)
    clean_name = name.strip()
    print(f"Processing : {clean_name}")