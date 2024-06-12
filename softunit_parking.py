number_of_commands = int(input())

users = {}

for _ in range(number_of_commands):
    command = input().split()
    task = command[0]
    name = command[1]
    if task == "register":
        number = command[2]
        if name not in users:
            users[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {users[name]}")
    elif task == "unregister":
        if name in users:
            print(f"{name} unregistered successfully")
            del users[name]
        else:
            print(f"ERROR: user {name} not found")

for key, value in users.items():
    print(f"{key} => {value}")
