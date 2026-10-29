import ast
import os

FILE_NAME = "attendance.txt"
REQUIRED_PERCENTAGE = 75
students = []


def load_students():
    """Load student records from attendance.txt."""
    global students
    students = []
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            try:
                record = ast.literal_eval(line.strip())
                if isinstance(record, dict):
                    students.append(record)
            except (ValueError, SyntaxError):
                continue


def save_students():
    """Save all student records to attendance.txt."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for student in students:
            file.write(repr(student) + "\n")


def find_student(roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def attendance_percent(student):
    if student["held"] == 0:
        return 0.0
    return student["attended"] / student["held"] * 100


def add_student():
    roll_text = input("Roll: ").strip()
    if not roll_text.isdigit() or int(roll_text) <= 0:
        print("Invalid roll number. Enter a positive number.")
        return

    roll = int(roll_text)
    if find_student(roll):
        print(f"Roll number {roll} already exists.")
        return

    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    student = {"roll": roll, "name": name, "held": 0, "attended": 0}
    students.append(student)
    students.sort(key=lambda item: item["roll"])
    save_students()
    print(
        f"Student added: {roll} | {name} | "
        f"Held: {student['held']} | Attended: {student['attended']}"
    )


def mark_attendance():
    roll_text = input("Roll: ").strip()
    if not roll_text.isdigit() or int(roll_text) <= 0:
        print("Invalid roll number. Enter a positive number.")
        return

    roll = int(roll_text)
    student = find_student(roll)
    if student is None:
        print(f"Roll number {roll} not found.")
        return

    status = input("Status (P/A): ").strip().upper()
    if status not in ("P", "A"):
        print("Invalid status. Enter P or A.")
        return

    student["held"] += 1
    if status == "P":
        student["attended"] += 1

    save_students()
    print(f"Attendance marked: {student['name']} | Status: {status}")


def show_percentage():
    roll_text = input("Roll: ").strip()
    if not roll_text.isdigit() or int(roll_text) <= 0:
        print("Invalid roll number. Enter a positive number.")
        return

    roll = int(roll_text)
    student = find_student(roll)
    if student is None:
        print(f"Roll number {roll} not found.")
        return

    if student["held"] == 0:
        print(f"{student['name']}: Attendance 0.00% (no classes held yet)")
    else:
        print(
            f"{student['name']}: Attendance "
            f"{attendance_percent(student):.2f}%"
        )


def show_shortage_list():
    below = [
        student for student in students
        if student["held"] > 0
        and attendance_percent(student) < REQUIRED_PERCENTAGE
    ]
    below.sort(key=lambda item: (attendance_percent(item), item["roll"]))

    if not below:
        print("No students are below 75% attendance.")
        return

    print("Below 75%:")
    for student in below:
        print(
            f"{student['roll']} | {student['name']} | "
            f"{attendance_percent(student):.2f}%"
        )


def list_students():
    if not students:
        print("No students found.")
        return

    print("Roll | Name | Held | Attended | Attendance")
    for student in students:
        print(
            f"{student['roll']} | {student['name']} | "
            f"{student['held']} | {student['attended']} | "
            f"{attendance_percent(student):.2f}%"
        )


def main():
    load_students()
    while True:
        print("\n===== Student Attendance Manager =====")
        print("1. Add student")
        print("2. Mark attendance (P/A)")
        print("3. Show attendance percentage")
        print("4. Show shortage list (below 75%)")
        print("5. List all students")
        print("6. Exit")

        choice = input("Enter menu option: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            show_percentage()
        elif choice == "4":
            show_shortage_list()
        elif choice == "5":
            list_students()
        elif choice == "6":
            save_students()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()