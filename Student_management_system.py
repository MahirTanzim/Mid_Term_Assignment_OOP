class StudentDatabase:
    student_list = []  

    @classmethod
    def add_student(self, student_data):
        self.student_list.append(student_data)


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self._student_id = student_id
        self._name = name
        self._department = department
        self._is_enrolled = is_enrolled
        student_data = {
            'student_id': self._student_id,
            'name': self._name,
            'department': self._department,
            'is_enrolled': self._is_enrolled
        }
        StudentDatabase.add_student(student_data)


        def enroll_student(self):
            if self._is_enrolled:
                print(f"Student {self._student_id} is already enrolled.")
            else:
                self._is_enrolled = True
                print(f"Student {self._student_id} has been enrolled.")
        
        def drop_student(self):
            if not self._is_enrolled:
                print(f"Student {self._student_id} is already Droped.")
            else:
                self._is_enrolled = False
                print(f"Student {self._student_id} has been dropped.")


def menu():
    while True:
        print("\n----- Student Management System -----")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
                print("\n| {:<10} | {:<20} | {:<20} | {:<12} |".format("ID", "Name", "Department", "Status"))
                print("-" * 75)
                


        elif choice == '2':
            pass
        elif choice == '3':
            pass

        elif choice == '4':
            pass
        else:
            print("Invalid choice. Please try again.")

menu()

st1 = Student(101, "Mahir", "CSE", True)
print(StudentDatabase.student_list[0]["name"])