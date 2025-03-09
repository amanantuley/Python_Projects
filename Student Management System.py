'''
      
            Name : Antuley Aman Siraj
            Roll No : 23CO25
            Batch - 01


                *Mini-Project*
            Topic : Student Management System

'''



students = []  

def add_student(name, roll_no, marks):
    student = {"Name": name, "Roll No": roll_no, "Marks": marks}
    students.append(student)
    print(f"Student {name} added successfully!\n")

def remove_student(roll_no):
    global students
    students = [s for s in students if s["Roll No"] != roll_no]
    print(f"Student with Roll No {roll_no} removed successfully!\n")

def update_student(roll_no, new_marks):
    for student in students:
        if student["Roll No"] == roll_no:
            student["Marks"] = new_marks
            print(f"Marks updated for Roll No {roll_no}!\n")
            return
    print(f"Student with Roll No {roll_no} not found!\n")

def display_students():
    if not students:
        print("No students in the record.\n")
        return
    print("Student Records:")
    for student in students:
        print(f"Name: {student['Name']}, Roll No: {student['Roll No']}, Marks: {student['Marks']}")
    print()

add_student("Aman", 25, 95)
add_student("Asim", 26, 90)
display_students()

update_student(101, 95)
remove_student(26)
display_students()

# Conclusion : 