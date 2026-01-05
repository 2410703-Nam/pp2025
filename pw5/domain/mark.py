def input_marks(students, courses):
    marks = {}

    with open("marks.txt", "w", encoding="utf-8") as f:
        for course in courses:
            cid = course["id"]
            marks[cid] = {}

            for student in students:
                mark = float(input(
                    f"Mark for {student['name']} ({course['name']}): "
                ))
                marks[cid][student["id"]] = mark
                f.write(f"{cid},{student['id']},{mark}\n")

    return marks