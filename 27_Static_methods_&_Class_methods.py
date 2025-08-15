
class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getinfo(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")


print(Employee.is_valid_position("Rocket Scientist"))
print(employee1.getinfo())



class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method:
    def getinfo(self):
        return f"{self.name} {self.gpa}"
    
    #Class method:
    @classmethod
    def get_count(cls):
        return f"Total number of students = {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    

student1 = Student("Spongebob", 3.2)
student2 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.getinfo(student1))
print(Student.get_average_gpa())