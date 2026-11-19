# Commission employee subclass
from employee import Employee


class CommissionEmployee(Employee):

    def __init__(self, name, base_salary, commission):
        super().__init__(name)
        self.base_salary = base_salary
        self.commission = commission

    def calculate_pay(self):
        return self.base_salary + self.commission
