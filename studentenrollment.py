class Student:
    def _init_(self, student_id, name):
        """Constructor to initialize a student with ID and name."""
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []  # List to store courses the student is enrolled in

    def enroll(self, course):
        """Enroll the student in a course."""
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.name} has been enrolled in {course}.")
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def display_info(self):
        """Display student's information."""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Enrolled Courses:", ", ".join(self.enrolled_courses) if self.enrolled_courses else "None")


class EnrollmentSystem:
    def _init_(self):
        """Constructor to initialize the enrollment system with no students."""
        self.students = {}  # Dictionary to store students by their ID

    def add_student(self, student_id, name):
        """Add a new student to the system."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} has been added with ID {student_id}.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def enroll_student(self, student_id, course):
        """Enroll a student in a course."""
        if student_id in self.students:
            student = self.students[student_id]
            student.enroll(course)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students(self):
        """Display information for all students."""
        if self.students:
            print("Student Information:")
            for student in self.students.values():
                student.display_info()
                print("-" * 20)
        else:
            print("No students in the system.")


# Example Usage
system = EnrollmentSystem()

# Adding students
system.add_student(1, "Alice")
system.add_student(2, "Bob")

# Enrolling students in courses
system.enroll_student(1, "Math")
system.enroll_student(1, "Science")
system.enroll_student(2, "Math")
system.enroll_student(1, "Math")  # Attempt to re-enroll in the same course

# Displaying all students
system.display_all_students()