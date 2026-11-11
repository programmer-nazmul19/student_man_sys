student_names = {"nazmul": "80", "arafat": "90", "sabbir": "85", "shakil": "75", "rakib": "95"}
print(student_names["arafat"])
def grade_analysis(name):
    name = name.strip().lower()
    if name in student_names:
        student_grade = int(student_names[name])
        if student_grade >= 90 and student_grade <= 100:
            print(f"Student {name} has an A+ grade.")
        elif student_grade >= 80 and student_grade < 90:
            print(f"Student {name} has an A grade.")
        elif student_grade >= 70 and student_grade < 80:
            print(f"Student {name} has an  A- grade.")
        elif student_grade >= 60 and student_grade < 70:
            print(f"Student {name} has a B grade.")
        elif student_grade >= 50 and student_grade < 60:
            print(f"Student {name} has a B- grade.")
        elif student_grade >= 40 and student_grade < 50:
            print(f"Student {name} has a C grade.")
        elif student_grade >= 33 and student_grade < 40:
            print(f"Student {name} has a D grade.")
        elif student_grade < 33:
            print(f"Student {name} has failed the exam.")
        
    else:
        print(f"Student {name} not found in the system.")

def main():
    while True:
        print("1. Grade Analysis")
        input_choice = input("Enter your choice (1 to exit): ")
        if input_choice == "1":
            name = input("Enter student name for grade analysis: ")
            grade_analysis(name)

if __name__ == "__main__":
    main()
