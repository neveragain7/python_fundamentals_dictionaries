command = input()

companies = {}

while not command == "End":
    data = command.split(" -> ")
    company_name, employee_id = data
    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

    command = input()

sorted_companies = sorted(companies.items(), key=lambda kvp: kvp[0])

for key, value in sorted_companies:
    print(f"{key}")
    for name in value:
        print(f"-- {name}")
