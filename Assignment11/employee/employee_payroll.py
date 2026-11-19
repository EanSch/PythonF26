# Imports for employee classes
from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalaryEmployee
from commission_employee import CommissionEmployee


# Dictionary to store employees by department
departments = {
    "Sales": [
        HourlyEmployee("Nick DeFalco", 25, 2080),
        SalaryEmployee("AppleJack Johnson", 44000),
        SalaryEmployee("Mario Dubois", 77200)
    ],

    "Engineering": [
        SalaryEmployee("Anthony Jo", 98000),
        Employee("Stephanie Johnson", 31200)
    ],

    "Maintenance": [
        CommissionEmployee("Dominic Togo", 20000, 45000),
        HourlyEmployee("Christina Gonzalez", 19.8, 2080)
    ],

    "HR": [
        HourlyEmployee("Geoffrey Dav", 65, 2080)
    ]
}


# Display payroll by department
for department, employees in departments.items():
    print(f"\nDepartment: {department}")

    total_payroll = 0

    for employee in employees:
        pay = employee.calculate_pay()
        total_payroll += pay

        print(f"    {employee.name} ({type(employee).__name__}): ${pay:.2f}")

        # Display commission breakdown
        if isinstance(employee, CommissionEmployee):
            percentage = (employee.commission / pay) * 100

            print(f"        Base ${employee.base_salary:.2f} + Commission ${employee.commission:.2f} ({percentage:.1f}% of earnings)")

    print(f"Total Payroll: ${total_payroll:.2f}")
