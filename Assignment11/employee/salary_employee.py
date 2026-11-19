# Salary employee subclass
from unicodedata import name

from employee import Employee


class SalaryEmployee(Employee):

    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary
