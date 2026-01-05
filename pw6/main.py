from input import input_students, input_courses, input_marks
from output import show_students, show_courses, show_marks, show_gpa
from domain.gpa import GPA
from domain.storage import save_data, load_data

def main():
    data = load_data()

    if data:
        print("Loaded data from students.dat")
        students = data["students"]
        courses = data["courses"]
        marks = data["marks"]
    else:
        students = input_students()
        courses = input_courses()
        marks = input_marks(students, courses)

    show_students(students)
    show_courses(courses)
    show_marks(students, courses, marks)

    gpa_obj = GPA(marks, courses, students)
    show_gpa(students, gpa_obj.gpa)

    save_data({
        "students": students,
        "courses": courses,
        "marks": marks
    })
    print("Data compressed and saved to students.dat")

if __name__ == "__main__":
    main()