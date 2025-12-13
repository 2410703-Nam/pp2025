class Mark:
    def __init__(self):
        self.marks = {}

    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.marks[course_id][student_id] = mark
