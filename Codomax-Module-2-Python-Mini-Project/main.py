# ==========================================
# Student Management System Pro
# Codomax Digital Solutions Internship
# Module 2 - Python Mini Project
# Author: Jerome Christopher J
# ==========================================

from student_manager import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    student_statistics
)


def display_menu():
    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM PRO")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Exit")
    print("=" * 45)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            student_statistics()

        elif choice == "7":
            print("\nThank you for using Student Management System Pro.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()