class GPA:
    def __init__(self, marks, courses, students):
        self.gpa = self.calculate(marks, courses, students)

    def calculate(self, marks, courses, students):
        gpa_dict = {}

        for student in students:
            sid = student['id']
            total_points = 0
            total_credits = 0

            for course in courses:
                cid = course['id']
                credits = float(course['credits'])

                if cid in marks and sid in marks[cid]:
                    total_points += marks[cid][sid] * credits
                    total_credits += credits

            gpa_dict[sid] = total_points / total_credits if total_credits else 0

        return gpa_dict
