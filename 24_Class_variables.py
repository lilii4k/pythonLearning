class Student:

    class_year = 2024
    num_students = 0
    all_students = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        Student.all_students.append(self)

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)

print(student1.name, student2.age)
print(Student.class_year)
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students in it:")
for student in Student.all_students:
    print(student.name)