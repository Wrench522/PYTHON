import re


# =========================
# 1. PERSON (BASE CLASS)
# =========================
class Person:
    def __init__(self, name, admission_number):
        self._name = name
        self.admission_number = admission_number  # uses setter validation

    @property
    def name(self):
        return self._name

    @property
    def admission_number(self):
        return self._admission_number

    @admission_number.setter
    def admission_number(self, value):
        # Format: ADM/2026/001
        pattern = r"^ADM/\d{4}/\d{3}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid admission number format. Expected ADM/YYYY/XXX")
        self._admission_number = value


# =========================
# 2. SUBJECT (COMPOSITION)
# =========================
class Subject:
    def __init__(self, subject_name, marks):
        self.subject_name = subject_name
        self.marks = marks  # uses setter validation

    @staticmethod
    def is_valid_mark(value):
        return 0 <= value <= 100

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not Subject.is_valid_mark(value):
            raise ValueError(f"Invalid mark {value}. Must be between 0 and 100.")
        self._marks = value

    def has_passed(self):
        return self.marks >= Student.pass_mark


# =========================
# 3. STUDENT CLASS
# =========================
class Student(Person):
    total_students = 0
    pass_mark = 50

    def __init__(self, name, admission_number, subjects):
        super().__init__(name, admission_number)

        if len(subjects) != 3:
            raise ValueError("Student must have exactly 3 subjects.")

        self.subjects = subjects
        Student.total_students += 1

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    def calculate_total(self):
        return sum(s.marks for s in self.subjects)

    def calculate_average(self):
        return self.calculate_total() / len(self.subjects)

    def determine_grade(self):
        avg = self.calculate_average()
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "E"

    def pass_or_fail(self):
        return self.calculate_average() >= Student.pass_mark

    def generate_report_card(self):
        print("\n================ REPORT CARD ================")
        print(f"Name: {self.name}")
        print(f"Admission No: {self.admission_number}")

        for s in self.subjects:
            print(f"{s.subject_name}: {s.marks}")

        print("--------------------------------------------")
        print(f"Total: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.determine_grade()}")
        print(f"Result: {'PASS' if self.pass_or_fail() else 'FAIL'}")
        print("============================================\n")

    def __str__(self):
        return f"{self.name} ({self.admission_number}) - Avg: {self.calculate_average():.2f}"

    def __lt__(self, other):
        return self.calculate_average() < other.calculate_average()


# =========================
# 4. HONOURS STUDENT (POLYMORPHISM)
# =========================
class HonoursStudent(Student):
    def determine_grade(self):
        avg = self.calculate_average()
        if avg >= 85:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 65:
            return "C"
        elif avg >= 55:
            return "D"
        else:
            return "E"


# =========================
# 5. PROGRAM EXECUTION
# =========================

students = []

# Helper function to safely create subjects
def create_subject(name, mark):
    try:
        return Subject(name, mark)
    except ValueError as e:
        print(f"Error creating subject '{name}': {e}")
        return Subject(name, 0)  # fallback safe mark


# Create Students
students.append(
    Student(
        "Alice",
        "ADM/2026/001",
        [
            create_subject("Mathematics", 78),
            create_subject("English", 65),
            create_subject("Computer Studies", 88),
        ],
    )
)

students.append(
    Student(
        "Brian",
        "ADM/2026/002",
        [
            create_subject("Mathematics", 45),
            create_subject("English", 55),
            create_subject("Computer Studies", 60),
        ],
    )
)

students.append(
    Student(
        "Clara",
        "ADM/2026/003",
        [
            create_subject("Mathematics", 90),
            create_subject("English", 85),
            create_subject("Computer Studies", 92),
        ],
    )
)

students.append(
    HonoursStudent(
        "David",
        "ADM/2026/004",
        [
            create_subject("Mathematics", 88),
            create_subject("English", 82),
            create_subject("Computer Studies", 91),
        ],
    )
)

# Invalid marks case (trigger exception)
students.append(
    Student(
        "Eve",
        "ADM/2026/005",
        [
            create_subject("Mathematics", 150),  # invalid → handled
            create_subject("English", 70),
            create_subject("Computer Studies", 75),
        ],
    )
)


# =========================
# DISPLAY REPORT CARDS
# =========================
for s in students:
    s.generate_report_card()

# =========================
# RANKING (USING __lt__)
# =========================
best = max(students)
weakest = min(students)

print("===== PERFORMANCE SUMMARY =====")
print("Best Student:", best)
print("Weakest Student:", weakest)

# =========================
# TOTAL STUDENTS
# =========================
print("\nTotal students created:", Student.get_total_students())