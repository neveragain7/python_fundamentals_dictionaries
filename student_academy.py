number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = grade
    else:
        new_grade = (students[student] + grade) / 2
        students[student] = new_grade

passed_students = {student: grade for student, grade in students.items() if grade >= 4.50}

sorted_students = sorted(passed_students.items(), key=lambda kvp: -kvp[1])

for key, value in sorted_students:
    print(f"{key} -> {value:.2f}")
