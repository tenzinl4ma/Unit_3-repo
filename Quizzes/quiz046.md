# Question

<img width="1040" alt="Screenshot 2025-02-24 at 2 10 05 PM" src="https://github.com/user-attachments/assets/0c132163-0bb4-46a5-a4c0-573fd7753bb1" />


# Code

```.py
class Citizen:
    def __init__(self, name: str, city: str, status: str):
        self.name = name
        self.city = city
        self.status = status

    def get_name(self) -> str:
        return self.name

    def get_city(self) -> str:
        return self.city

    def get_status(self) -> str:
        return self.status


class Employee(Citizen):
    def __init__(self, name: str, city: str, status: str, annual_salary: float):
        super().__init__(name, city, status)
        self.annual_salary = annual_salary

    def get_annual_salary(self) -> float:
        return self.annual_salary


class PartTimeEmployee(Employee):
    def __init__(self, name: str, city: str, status: str, annual_salary: float, fraction: float, union_member: bool):
        super().__init__(name, city, status, annual_salary)
        self.fraction = fraction
        self.union_member = union_member

    def get_fraction(self) -> float:
        return self.fraction

    def is_union_member(self) -> bool:
        return self.union_member


# Example Usage:
part_time_emp = PartTimeEmployee("Alice", "New York", "Active", 50000, 0.5, True)
print(f"Name: {part_time_emp.get_name()}")
print(f"City: {part_time_emp.get_city()}")
print(f"Status: {part_time_emp.get_status()}")
print(f"Annual Salary: {part_time_emp.get_annual_salary()}")
print(f"Fraction Worked: {part_time_emp.get_fraction()}")
print(f"Union Member: {part_time_emp.is_union_member()}")

```

# Evidence

<img width="1305" alt="Screenshot 2025-02-24 at 8 41 55 PM" src="https://github.com/user-attachments/assets/3aec4325-8220-4e4c-9108-deaa8bb4653e" />

# UML Diagram

![Screenshot 2025-02-24 at 8 42 18 PM](https://github.com/user-attachments/assets/a36db1b8-89de-49d3-8ec2-e584f76a9214)
