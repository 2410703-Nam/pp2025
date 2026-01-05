def input_courses():
    courses = []
    n = int(input("Enter number of courses: "))

    for _ in range(n):
        courses.append({
            "id": input("Course ID: "),
            "name": input("Course name: "),
            "credits": input("Credits: ")
        })

    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c['id']},{c['name']},{c['credits']}\n")

    return courses