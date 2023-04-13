# Aggregation
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return f"{self.pay * 12}"


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return f"Total Aggregation: {int(self.pay.get_total()) + self.bonus}"


salary = Salary(100)
employee = Employee(salary, 10)
print(employee.annual_salary())


# Composition
class SalaryComposition:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return f"{self.pay*12}"


class EmployeeComposition:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annual_salary(self):
        return f"Total Composition: {int(self.salary.get_total()) + self.bonus}"


employee = EmployeeComposition(100, 10)
print(employee.annual_salary())
