# Initialize an empty student list
student_list = []

# Part (a): Function to add a student
def add_student(student_list, student_id, name, age, course):
    # Check if student ID is unique
    for student in student_list:
        if student['ID'] == student_id:
            print(f"Error: Student with ID {student_id} already exists.")
            return
    # Add new student as a dictionary
    new_student = {'ID': student_id, 'Name': name, 'Age': age, 'Course': course}
    student_list.append(new_student)
    print(f"Student {name} added successfully.")

# Part (b): Functions to find and remove a student by ID
def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student['ID'] == student_id:
            return student
    print(f"Error: Student with ID {student_id} not found.")
    return None

def remove_student_by_id(student_list, student_id):
    for i, student in enumerate(student_list):
        if student['ID'] == student_id:
            removed_student = student_list.pop(i)
            print(f"Student {removed_student['Name']} removed successfully.")
            return
    print(f"Error: Student with ID {student_id} not found.")

# Part (c): Classes for Person, Student, and Instructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    
    def study(self):
        return f"Student is studying {self.course}"

class Instructor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        return f"Instructor is teaching {self.subject}"

# Demonstrating polymorphism
student = Student("Alice", 20, "Mathematics")
instructor = Instructor("Dr. Smith", 45, "Physics")

print(student.get_details())
print(student.study())
print(instructor.get_details())
print(instructor.teach())

# Part (d): Higher-order function to sort students
def sort_students(student_list, key_function):
    return sorted(student_list, key=key_function)

# Example usage:
# Adding some students to the list for testing
add_student(student_list, 1, "Calvin", 20, "Mathematics")
add_student(student_list, 2, "Mark", 22, "Computer Science")
add_student(student_list, 3, "Peter", 21, "Physics")

# Sorting by age
sorted_by_age = sort_students(student_list, key_function=lambda student: student['Age'])
print("Sorted by age:", sorted_by_age)

# Sorting by name
sorted_by_name = sort_students(student_list, key_function=lambda student: student['Name'])
print("Sorted by name:", sorted_by_name)
