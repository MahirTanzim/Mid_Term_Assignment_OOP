# 1. Create the StudentDatabase class

class StudenDatabase:
    student_list = []

    @classmethod
    def add_student(self, name, id, cls):
        self.student_list.append({"Name": name, "ID" : id, "Class": cls})


StudenDatabase.add_student("Mahir", 1001, 10)
StudenDatabase.add_student("Maisha", 1002, 12)

print(StudenDatabase.student_list)