courses = {}

command = input()

while not command == "end":
    data = command.split(" : ")
    course, student = data
    if course not in courses:
        courses[course] = []
        courses[course].append(student)
    else:
        courses[course].append(student)
    command = input()

sorted_courses = sorted(courses.items(), key=lambda kvp: -len(kvp[1]))
for key, value in sorted_courses:
    sorted_names = sorted(value)
    count = len(value)
    print(f"{key}: {count}")
    for name in sorted_names:
        print(f"-- {name}")
