# Student Management System

students = {}

# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


# Function to add student
def add_student():
    roll_no = int(input("Enter Roll Number: "))

    if roll_no in students:
        print("Roll Number already exists!")
        return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks of Subject {i}: "))
        marks.append(mark)

    percentage = sum(marks) / 5
    grade = calculate_grade(percentage)

    students[roll_no] = {
        "Name": name,
        "Marks": marks,
        "Percentage": percentage,
        "Grade": grade
    }

    print("Student record added successfully.")


# Function to view all students
def view_all():
    if len(students) == 0:
        print("No records found.")
    else:
        print("\n----- STUDENT RECORDS -----")
        for roll_no, data in students.items():
            print("\nRoll Number :", roll_no)
            print("Name :", data["Name"])
            print("Marks :", data["Marks"])
            print("Percentage :", round(data["Percentage"], 2))
            print("Grade :", data["Grade"])


# Function to search student
def search_student():
    roll_no = int(input("Enter Roll Number to search: "))

    if roll_no in students:
        data = students[roll_no]

        print("\nStudent Found")
        print("Name :", data["Name"])
        print("Marks :", data["Marks"])
        print("Percentage :", round(data["Percentage"], 2))
        print("Grade :", data["Grade"])

    else:
        print("Student not found.")


# Function to update student
def update_student():
    roll_no = int(input("Enter Roll Number to update: "))

    if roll_no in students:

        name = input("Enter new name: ")

        marks = []
        for i in range(1, 6):
            mark = float(input(f"Enter new marks of Subject {i}: "))
            marks.append(mark)

        percentage = sum(marks) / 5
        grade = calculate_grade(percentage)

        students[roll_no] = {
            "Name": name,
            "Marks": marks,
            "Percentage": percentage,
            "Grade": grade
        }

        print("Record updated successfully.")

    else:
        print("Student not found.")


# Function to delete student
def delete_student():
    roll_no = int(input("Enter Roll Number to delete: "))

    if roll_no in students:
        del students[roll_no]
        print("Record deleted successfully.")
    else:
        print("Student not found.")


# Function to display menu
def show_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


# Main Program
while True:
    show_menu()

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_all()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid choice! Please try again.")