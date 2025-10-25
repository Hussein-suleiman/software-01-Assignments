class Student :
    def __init__(self, name,gender):
        self.name = name
        self.gender= gender

class Teacher :
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print (student.name + ' added successfully')
        return

    def remove_student(self, student):
        self.students.remove(student)
        print (student.name + ' removed successfully')
        return

    def attendance(self,student):
        for i in range(student.students):
            print (self.students[i].name)
        return

student1 = Student("Hussein ", "male")
student2 = Student("Sulley", "female")
teacher = Teacher()
teacher.add_student(student1)
teacher.add_student(student2)
teacher.remove_student(student2)





