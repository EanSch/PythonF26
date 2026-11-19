# Parent class for all employees
class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary