
class student:
    def displaydetails(self):
       print("name:",self.name)
       print("age:",self.age)
       print("marks:",self.marks)
          
student1=student()
student1.name="yazhu"
student1.age=18
student1.marks=99

student1.displaydetails()



class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of the employee is:", self.name)
        print("Age of the employee is:", self.age)
        print("Salary of the employee is:", self.salary)
        print("Gender of the employee is:", self.gender)


emp = Employee("yazhu", 20, 100000, "female")
emp.employee_details()
