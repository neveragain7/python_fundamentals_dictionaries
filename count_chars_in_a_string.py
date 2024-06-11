data = input().split()

dictionary = {}

for word in data:
    for letter in word:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
