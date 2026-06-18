class Student:

    def __init__(self, student_id, student_name, course, marks):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.marks = marks

    # method to calculate grade
    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "E"

    # method to display details
    def display_details(self):
        print("Student Id:", self.student_id)
        print("Student Name:", self.student_name)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
        print("-------------------------")


# objects (OUTSIDE the class)
s1 = Student("001", "Mark", "ICT", 60)
s2 = Student("002", "John", "Plumbing", 30)
s3 = Student("003", "Wrench", "HR", 86)

s1.display_details()
s2.display_details()
s3.display_details()