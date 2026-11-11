import json

student_name = {}

# Save student data
def save_students():
    with open("students.json", "w") as file:
        json.dump(student_name, file, indent=4)


# Load student data
def load_students():
    global student_name

    try:
        with open("students.json", "r") as file:
            student_name = json.load(file)

    except FileNotFoundError:
        student_name = {}
# add student 
def add_student(name, grade):
    if name in student_name:
        print(f"student {name} already exists in the system.")
    else:
        student_name[name] = grade
        print(f"student {name} with grade {grade} has been added successfully.")
        save_students()  # Save the updated student data to the file

# update student grade
def update_student(name, grade):
    if name in student_name:
        student_name[name] = grade
        print(f"student {name} grade has been updated to {grade}.")
        save_students()  # Save the updated student data to the file
    else:
        print(f"student {name} does not exist in the system.")

# delete student
def delete_student(name):
    if name in student_name:
        del student_name[name]
        print(f"student {name} has been deleted successfully.")
        save_students()  # Save the updated student data to the file
    else:
        print(f"student {name} does not exist in the system.")

# view all students

def view_students():
    if student_name:
        print("List of students and their grades:")
        for name, grade in student_name.items():
            print(f"{name}: {grade}")
    else:
        print("student not found in the system.")

def main():
    load_students()  # Load existing student data from the file
    while True:
        print("\n======Student Management System======")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): \n")
        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == "2":
            name = input("Enter student name: ")
            grade = input("Enter new student grade: ")
            update_student(name, grade)
        elif choice == "3":
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("Exiting the Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()