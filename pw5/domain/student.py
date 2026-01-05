def input_students():
    students = []
    n = int(input("Enter number of students: "))

    for _ in range(n):
        students.append({
            "id": input("Student ID: "),
            "name": input("Student name: "),
            "dob": input("Date of birth: ")
        })

    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s['id']},{s['name']},{s['dob']}\n")

    return students