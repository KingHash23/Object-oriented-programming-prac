class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department
        self.task = None  # Initialize task to None

    def assign_task(self, task):
        if self.task:
            return f"{self.name} is already assigned the task '{self.task}'."
        else:
            self.task = task
            return f"{self.name} has been assigned the task '{self.task}'."

    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
            f"Employee ID: {self.employee_id}, Department: {self.department}, "
            f"Task: {self.task if self.task else 'No task assigned'}"
        )


# Creating two Employee objects
emp1 = Employee("John", 25, "Male", 123, "HR")
emp2 = Employee("Jane", 30, "Female", 456, "Sales")

# Assigning tasks
print(emp1.assign_task("Data analysis"))
print(emp2.assign_task("Marketing"))

# Displaying employee information
print(emp1.display_info())
print(emp2.display_info())
