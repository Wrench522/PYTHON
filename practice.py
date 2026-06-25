# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Child class Teacher
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}, Salary: {self.salary}")


# Child class Student
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Grade: {self.grade}")


# Main program
teacher1 = Teacher("Alice", 35, "Mathematics", 50000.0)
student1 = Student("Bob", 18, "S12345", "A")

teacher1.display_info()
student1.display_info()