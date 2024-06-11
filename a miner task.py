command = input()
counter = 0
resources = {}

while not command == "stop":
    counter += 1
    if not counter % 2 == 0:
        resource = command
        if resource not in resources:
            resources[resource] = 0
    else:
        quantity = int(command)
        resources[resource] += quantity
    command = input()

for key, value in resources.items():
    print(f"{key} -> {value}")