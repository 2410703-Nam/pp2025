def show_students(students):
    print("\nList of students:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DOB: {s['dob']}")


def show_courses(courses):
    print("\nList of courses:")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}, Credits: {c['credits']}")


def show_marks(students, courses, marks):
    for course in courses:
        cid = course['id']
        print(f"\nMarks for course {course['name']}:")

        for student in students:
            sid = student['id']
            value = marks.get(cid, {}).get(sid, "N/A")
            print(f"{student['name']} ({sid}): {value}")


def show_gpa(students, gpa):
    print("\nGPA of students:")
    for student in students:
        sid = student['id']
        print(f"{student['name']} ({sid}): GPA = {gpa[sid]:.2f}")
