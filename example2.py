# Version 2

class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  # Private attribute with getter/setter
        self._date_of_birth = date_of_birth  # Private attribute, read-only
        self._place_of_birth = place_of_birth  # Private attribute, read-only
    
    # Properties for name (can be changed)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.strip()
    
    # Properties for date_of_birth (read-only - you can't change when you were born!)
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    # Properties for place_of_birth (read-only - you can't change where you were born!)
    @property
    def place_of_birth(self):
        return self._place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."
    
# # Creating instances
# aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
# steve = Person("Steve Rich", "06/06/1998", "London")

# # Accessing properties through getters
# print(steve.talk())
# print(f"Name: {steve.name}")
# print(f"Date of birth: {steve.date_of_birth}")
# print(f"Place of birth: {steve.place_of_birth}")

# # We can change the name (has a setter)
# steve.name = "Steve Rich"
# print(f"Updated name: {steve.name}")

# # But we cannot change date_of_birth or place_of_birth (no setters)
# # These would raise AttributeError:
# # steve.date_of_birth = "07/07/1999"  # This would fail!
# # steve.place_of_birth = "Birmingham"  # This would fail!

class AdaStaff(Person):  # AdaStaff inherits from Person
    def __init__(self, name, date_of_birth, place_of_birth, employee_id, department):
        super().__init__(name, date_of_birth, place_of_birth)  # Call parent constructor
        self._employee_id = employee_id
        self._department = department

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def department(self):
        return self._department

    def work(self):
        return f"{self.name} is working in the {self.department} department."

    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Department: {self.department}"


# Create AdaStaff objects
teacher1 = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
teacher2 = AdaStaff("Mike Keddie", "21/03/1885", "London", "EMP002", "Education")
teacher3 = AdaStaff("Steve Rich", "07/09/1897", "Manchester", "EMP005", "Education")
admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")

# # Test the objects
# print(teacher1.talk())  # Inherited from Person
# print(teacher1.work())  # New method in AdaStaff
# print(teacher1.get_employee_info())

class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, student_id, course):
        super().__init__(name, date_of_birth, place_of_birth)
        self._student_id = student_id
        self._course = course
        self._grades = []  # Private list to store grades

    @property
    def student_id(self):
        return self._student_id

    @property
    def course(self):
        return self._course

    @property
    def grades(self):
        return self._grades

    def study(self):
        return f"{self.name} is studying {self.course}."

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    def get_average_grade(self):
        if self._grades:
            return sum(self._grades) / len(self._grades)
        return 0

    def get_student_info(self):
        return f"Student ID: {self.student_id}, Course: {self.course}, Average: {self.get_average_grade():.1f}"

# Create AdaStudent objects
student1 = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
student2 = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
student3 = AdaStudent("Mickey Mouse", "08/11/2007", "Sheffield", "STU003", "Cyber Security")
student4 = AdaStudent("Donald Duck", "08/11/2008", "Leeds", "STU004", "Tech BA")
student5 = AdaStudent("Minnie Mouse", "08/11/20010", "Oxford", "STU005", "Software Development")
student6 = AdaStudent("Snow White", "08/11/2009", "Cambridge", "STU006", "Data Science")
student7 = AdaStudent("Nick Wilde", "08/11/2003", "Cambridge", "STU007", "Data Science")
student8 = AdaStudent("Judy Hopps", "08/11/2008", "Cambridge", "STU008", "Data Science")
student9 = AdaStudent("Venelope VonShweetz", "08/11/2007", "Cambridge", "STU009", "Data Science")
student10 = AdaStudent("Fix-It Felix", "08/11/20012", "Cambridge", "STU0010", "Data Science")
student11 = AdaStudent("Slinky Dog", "08/11/2008", "Cambridge", "STU0011", "Data Science")




# Test the functionality
print(student1.talk())  # Inherited from Person
print(student1.study())  # New method in AdaStudent

# Add some grades
student1.add_grade(85)
student2.add_grade(92)
student3.add_grade(78)
student4.add_grade(67)
student5.add_grade(100)
student6.add_grade(97)
student7.add_grade(97)
student8.add_grade(97)
student9.add_grade(97)
student10.add_grade(97)
student11.add_grade(97)




# print(student1.get_student_info())

class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self.students = []  # List to store AdaStudent objects
    
    def add_student(self, student):
        if isinstance(student, AdaStudent):
            self.students.append(student)
            print(f"Added {student.name} to {self.cohort_code}")
        else:
            print("Can only add AdaStudent objects to cohort")
    
    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"Removed {student_name} from {self.cohort_code}")
                return
        print(f"Student {student_name} not found in {self.cohort_code}")
    
    def list_students(self):
        if not self.students:
            return f"No students in {self.cohort_code}"
        
        result = f"Students in {self.cohort_code}:\n"
        for student in self.students:
            result += f"- {student.name} ({student.course})\n"
        return result
    
    def search_student(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                return student
        return None
    
    def get_cohort_average(self):
        if not self.students:
            return 0
        
        total_average = 0
        students_with_grades = 0
        
        for student in self.students:
            avg = student.get_average_grade()
            if avg > 0:
                total_average += avg
                students_with_grades += 1
        
        return total_average / students_with_grades if students_with_grades > 0 else 0

# Create a cohort and add students
cohort1 = Cohort("DEV2024A")

# Add our existing students
cohort1.add_student(student1)
cohort1.add_student(student2)

# Create and add more students to reach our goal of 10+ objects
student3 = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
student4 = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")

cohort1.add_student(student3)
cohort1.add_student(student4)

# Test the cohort functionality
print(cohort1.list_students())

# Add some grades to the new students
student3.add_grade(88)
student3.add_grade(91)
student4.add_grade(76)
student4.add_grade(84)
student4.add_grade(89)

print(f"Cohort average: {cohort1.get_cohort_average():.1f}")

cohort2 = Cohort("DEV2027A")

cohort2.add_student(student9)
cohort2.add_student(student7)

print(cohort2.list_students())

student3.add_grade(88)
student3.add_grade(91)
student4.add_grade(76)
student4.add_grade(84)
student4.add_grade(89)


print(f"Cohort average: {cohort2.get_cohort_average():.1f}")