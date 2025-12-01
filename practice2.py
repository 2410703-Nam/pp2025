class Student:
    def input(students):
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
    
    def __init__(self):
        self.students = []
        Student.input(self.students)

    def listStudent(self):
        print("List of students:")
        for student in self.students:
            print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

class Course:
    def input(courses):
        n = input("Enter number of courses: ")
        for i in range(int(n)):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = {
                'id': id,
                'name': name
            }
            courses.append(course)
    
    def __init__(self):
        self.courses = []
        Course.input(self.courses)

    def listCourse(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course['id']}, Name: {course['name']}")

class Mark:
    def input(mark, students):
        cid = input("Enter course ID to input marks for: ")
        for student in students:
            markval = input(f"Enter mark for student {student['name']} (ID: {student['id']}): ")
            if cid not in mark:
                mark[cid] = {}
            mark[cid][student['id']] = float(markval)
    
    def __init__(self, students):
        self.mark = {}
        Mark.input(self.mark, students)

    def listMark(self, students):
        cid = input("Enter course ID to list marks for: ")
        print(f"Marks for course ID {cid}:")
        for sid, markval in self.mark[cid].items():
            sname = next((s['name'] for s in students if s['id'] == sid), "Unknown")
            print(f"Student ID: {sid}, Name: {sname}, Mark: {markval}")

student_obj = Student()
course_obj = Course()
mark_obj = Mark(student_obj.students)
student_obj.listStudent()
course_obj.listCourse()
mark_obj.listMark(student_obj.students)