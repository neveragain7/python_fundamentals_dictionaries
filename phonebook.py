phonebook_input = input()
dictionary = {}

while not phonebook_input.isnumeric():
    phonebook_list = phonebook_input.split("-")

    name = phonebook_list[0]
    number = phonebook_list[1]

    dictionary[name] = number

    phonebook_input = input()

for _ in range(int(phonebook_input)):
    name_input = input()

    if name_input in dictionary:
        print(f'{name_input} -> {dictionary[name_input]}')
    else:
        print(f'Contact {name_input} does not exist.')