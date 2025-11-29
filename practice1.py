students= []
courses = []
mark = {}

def inputStudent():
    n = input("Enter number of students: ")
    for i in range(int(n)):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = {
            'id': id,
            'name': name,
            'dob': dob
        }
        students.append(student)

def inputCourse():
    n = input("Enter number of courses: ")
    for i in range(int(n)):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = {
            'id': id,
            'name': name
        }
        courses.append(course)

def inputMark(): 
    cid = input("Enter course ID to input marks for: ")
    for student in students:
        mark_value = input(f"Enter mark for student {student['name']} (ID: {student['id']}): ")
        if cid not in mark:
            mark[cid] = {}
        mark[cid][student['id']] = float(mark_value)

def listStudent():
    print("List of students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

def listCourse():
    print("List of courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def listMark():
    cid = input("Enter course ID to list marks for: ")
    print(f"Marks for course ID {cid}:")
    for student_id, mark_value in mark[cid].items():
        student_name = next((s['name'] for s in students if s['id'] == student_id), "Unknown")
        print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark_value}")


inputStudent()
inputCourse()   
inputMark()
listStudent()
listCourse()
listMark()


