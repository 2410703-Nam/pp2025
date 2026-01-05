def input_students():
    students = []
    n = int(input("Enter number of students: "))
    for _ in range(n):
        students.append({
            'id': input("Enter student ID: "),
            'name': input("Enter student name: "),
            'dob': input("Enter student date of birth: ")
        })
    return students


def input_courses():
    courses = []
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        courses.append({
            'id': input("Enter course ID: "),
            'name': input("Enter course name: "),
            'credits': input("Enter course credits: ")
        })
    return courses


def input_marks(students, courses):
    marks = {}
    for course in courses:
        cid = course['id']
        print(f"Enter marks for course {course['name']} (ID: {cid}):")
        marks[cid] = {}

        for student in students:
            mark = float(input(
                f"Enter mark for student {student['name']} (ID: {student['id']}): "
            ))
            marks[cid][student['id']] = mark

    return marks
