from file_handler import load_students, save_students


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_student():
    students = load_students()

    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("\nStudent with this Roll Number already exists.")
        return

    name = input("Enter Student Name: ")

    python_marks = float(input("Enter Python Marks: "))
    ai_marks = float(input("Enter AI Marks: "))
    ml_marks = float(input("Enter Machine Learning Marks: "))

    total = python_marks + ai_marks + ml_marks
    average = total / 3
    grade = calculate_grade(average)

    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    students[roll_no] = {
        "name": name,
        "python": python_marks,
        "ai": ai_marks,
        "ml": ml_marks,
        "total": total,
        "average": round(average, 2),
        "grade": grade,
        "result": result
    }

    save_students(students)

    print("\nStudent added successfully!")
def view_students():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 90)
    print(f"{'Roll No':<10}{'Name':<20}{'Python':<10}{'AI':<10}{'ML':<10}{'Average':<10}{'Grade':<8}{'Result'}")
    print("=" * 90)

    for roll_no, student in students.items():
        print(
            f"{roll_no:<10}"
            f"{student['name']:<20}"
            f"{student['python']:<10}"
            f"{student['ai']:<10}"
            f"{student['ml']:<10}"
            f"{student['average']:<10}"
            f"{student['grade']:<8}"
            f"{student['result']}"
        )

    print("=" * 90)
def search_student():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    roll_no = input("Enter Roll Number to Search: ")

    if roll_no in students:
        student = students[roll_no]

        print("\n========== Student Details ==========")
        print(f"Roll Number : {roll_no}")
        print(f"Name        : {student['name']}")
        print(f"Python      : {student['python']}")
        print(f"AI          : {student['ai']}")
        print(f"ML          : {student['ml']}")
        print(f"Total       : {student['total']}")
        print(f"Average     : {student['average']}")
        print(f"Grade       : {student['grade']}")
        print(f"Result      : {student['result']}")
        print("=====================================")

    else:
        print("\nStudent not found.")
def update_student():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    roll_no = input("Enter Roll Number to Update: ")

    if roll_no not in students:
        print("\nStudent not found.")
        return

    student = students[roll_no]

    print("\nLeave the field blank to keep the current value.")

    name = input(f"Name ({student['name']}): ")
    python_marks = input(f"Python Marks ({student['python']}): ")
    ai_marks = input(f"AI Marks ({student['ai']}): ")
    ml_marks = input(f"Machine Learning Marks ({student['ml']}): ")

    if name:
        student["name"] = name

    if python_marks:
        student["python"] = float(python_marks)

    if ai_marks:
        student["ai"] = float(ai_marks)

    if ml_marks:
        student["ml"] = float(ml_marks)

    total = student["python"] + student["ai"] + student["ml"]
    average = total / 3

    student["total"] = total
    student["average"] = round(average, 2)
    student["grade"] = calculate_grade(average)
    student["result"] = "Pass" if average >= 50 else "Fail"

    students[roll_no] = student

    save_students(students)

    print("\nStudent updated successfully!")
def delete_student():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    roll_no = input("Enter Roll Number to Delete: ")

    if roll_no not in students:
        print("\nStudent not found.")
        return

    student = students[roll_no]

    print("\nStudent Found")
    print(f"Roll Number : {roll_no}")
    print(f"Name        : {student['name']}")

    confirm = input("\nAre you sure you want to delete this student? (Y/N): ")

    if confirm.lower() == "y":
        del students[roll_no]
        save_students(students)
        print("\nStudent deleted successfully!")
    else:
        print("\nDelete operation cancelled.")
def student_statistics():
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    total_students = len(students)

    total_average = 0
    pass_count = 0
    fail_count = 0

    highest_average = -1
    topper_name = ""

    for student in students.values():

        avg = student["average"]

        total_average += avg

        if avg > highest_average:
            highest_average = avg
            topper_name = student["name"]

        if student["result"] == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    class_average = total_average / total_students

    print("\n")
    print("=" * 45)
    print("        STUDENT STATISTICS")
    print("=" * 45)
    print(f"Total Students  : {total_students}")
    print(f"Top Performer   : {topper_name}")
    print(f"Highest Average : {highest_average:.2f}")
    print(f"Class Average   : {class_average:.2f}")
    print(f"Passed Students : {pass_count}")
    print(f"Failed Students : {fail_count}")
    print("=" * 45)