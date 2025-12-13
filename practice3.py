import math;
import numpy as np;

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
            credits = input("Enter course credits: ")
            course = {
                'id': id,
                'name': name,
                'credits': credits
            }
            courses.append(course)
    
    def __init__(self):
        self.courses = []
        Course.input(self.courses)

    def listCourse(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course['id']}, Name: {course['name']}, Credits: {course['credits']}")

class Mark: 
    def input(mark, students, courses):
        for course in courses:
            cid = course['id']
            print(f"Enter marks for course {course['name']} (ID: {cid}):")
            for student in students:
                markval = input(f"Enter mark for student {student['name']} (ID: {student['id']}): ")
                if cid not in mark:
                    mark[cid] = {}
            mark[cid][student['id']] = float(markval)
    
    def __init__(self, students, courses):
        self.mark = {}
        Mark.input(self.mark, students, courses)

    def listMark(self, students, courses):
        for course in courses:
            cid = course['id']
            print(f"Marks for course {course['name']} (ID: {cid}):")
            for student in students:
                sid = student['id']
                if cid in self.mark and sid in self.mark[cid]:
                    print(f"Student {student['name']} (ID: {sid}): Mark = {self.mark[cid][sid]}")
                else:
                    print(f"Student {student['name']} (ID: {sid}): Mark = N/A")

class GPA:
    def calculateGPA(marks, courses, students):
        gpa_dict = {}
        for student in students:
            sid = student['id']
            total_points = 0
            total_credits = 0
            for course in courses:
                cid = course['id']
                credits = float(course['credits'])
                if cid in marks and sid in marks[cid]:
                    mark = marks[cid][sid]
                    total_points += mark * credits
                    total_credits += credits
            if total_credits > 0:
                gpa = total_points / total_credits
                gpa_dict[sid] = gpa
            else:
                gpa_dict[sid] = 0
        return gpa_dict
    def __init__(self, marks, courses, students):
        self.gpa = GPA.calculateGPA(marks, courses, students)
    def listGPA(self, students):
        print("GPA of students:")
        for student in students:
            sid = student['id']
            print(f"Student {student['name']} (ID: {sid}): GPA = {self.gpa[sid]:.2f}")

student_obj = Student()
course_obj = Course()
mark_obj = Mark(student_obj.students, course_obj.courses)
student_obj.listStudent()
course_obj.listCourse()
mark_obj.listMark(student_obj.students, course_obj.courses)
gpa_obj = GPA(mark_obj.mark, course_obj.courses, student_obj.students)
gpa_obj.listGPA(student_obj.students)