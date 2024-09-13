class Student:
    def __init__(self, name, year, enrolled, gpa):
        self.name = name
        self.year = year
        self.enrolled = enrolled
        self.gpa = gpa

    def __str__(self):
        enrollment_status = 'Enrolled' if self.enrolled else 'Not Enrolled'
        return f"Student: {self.name}, Year: {self.year}, Status: {enrollment_status}, GPA: {self.gpa}"

    def display_info(self):
        print(f"The student {self.name}'s GPA is {self.gpa}!")

    def update_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
            print(f"{self.name}'s GPA has been updated to {self.gpa}.")
        else:
            print("Invalid GPA value. Please enter a GPA between 0.0 and 4.0.")

    def check_enrollment(self):
        if self.enrolled:
            print(f"{self.name} is currently enrolled.")
        else:
            print(f"{self.name} is not enrolled.")
            

# Creating instances of Student
student1 = Student('Alice', 'Sophomore', True, 3.8)
student2 = Student('Bob', 'Freshman', False, 2.7)

# Displaying information
student1.display_info()
student2.display_info()

# Checking enrollment status
student1.check_enrollment()
student2.check_enrollment()

# Updating GPA
student1.update_gpa(3.9)

# Printing student details using __str__ method
print(student1)
print(student2)
