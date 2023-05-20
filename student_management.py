import logging

logging.basicConfig(filename="student_management.log", level=logging.INFO)

class Faculty:
    def __init__(self, faculty_id):
        self.faculty_id = faculty_id

class StudentDetails:
    def __init__(self, student_id, first_name, last_name, contact_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.contact_number = contact_number




class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def main_menu(self):
        while True:
            print("\nMain Menu")
            print("1. Counsellor")
            print("2. Faculty")
            print("3. Exit")


            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.counsellor_menu()
            elif choice == "2":
                self.faculty_menu()
            elif choice == "3":
                print('Thank You')
                break
            else:
                print("Invalid choice. Please try again.")


    def counsellor_menu(self):
        while True:
            print("\nCounsellor Menu")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. View All Students")
            print("4. View Specific Student")
            print("5. Back to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.view_all_students()
            elif choice == "4":
                self.view_specific_student()
            elif choice == "5":
                self.main_menu()
                break
            else:
                print("Invalid choice. Please try again.")

    def faculty_menu(self):
        faculty_id = input("Enter Faculty ID: ")
        faculty = Faculty(faculty_id)

        while True:
            print("\nFaculty Menu")
            print("1. Add Student Marks")
            print("2. View Own Students")
            print("3. Back to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                faculty.add_student_marks(self.students)
            elif choice == "2":
                faculty.view_own_students(self.students)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("Student already exists with this ID.")
            return

        first_name = input("Enter First Name: ")
        if not first_name.isalpha():
            print("Invalid First Name. Please enter alphabetic characters only.")
            return

        last_name = input("Enter Last Name: ")
        if not last_name.isalpha():
            print("Invalid Last Name. Please enter alphabetic characters only.")
            return

        contact_number = input("Enter Contact Number: ")
        if not contact_number.isdigit():
            print("Invalid Contact Number. Please enter numeric characters only.")
            return

        self.students[student_id] = StudentDetails(student_id, first_name, last_name, contact_number)
        print("Student added successfully.")

    def remove_student(self):
        student_id = input("Enter Student ID to delete: ")
        if student_id not in self.students:
            print("Student does not exist.")
            return

        confirmation = input("Are you sure you want to delete the student? (Y/N)")
        if confirmation == 'Y':
            del self.students[student_id]
        else:
            print('Thank You!!')

    def view_all_students(self):
        # print(self.students)
        for i in self.students:
            print('student_id: ', i)
            print('first_name: ', (self.students[i]).first_name)
            print('last_name: ', (self.students[i]).last_name)
            print('contact_number: ', (self.students[i]).contact_number)
            print('\n')


    def view_specific_student(self):
        sid = input("Please Enter Student ID: ")

        single_student = self.students.get(sid)
        if single_student is not None:
            print(single_student)
        else:
            print("Student Does Not Exist")



if __name__ == '__main__':
    sm = StudentManagementSystem()
    sm.main_menu()