from platform import system_alias


class Employee:
    raise_amount = 1.5
    company_name ="Google"
    @classmethod
    def print_company_name(cls):
        print(f"the company name is {cls.company_name}")

    def __init__(self, first_name:str, last_name:str,mobile_number:int,salary:float):
        self.first_name =first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.salary = salary
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    def __repr__(self):
        return f"The first name is {self.first_name}, the last name is {self.last_name} the phone number is {self.mobile_number} the salary is {self.salary}"
    @staticmethod
    def week_day_off():
        print("this employee's week dat off is saturday and sunday")
    def increment(self):
        return self.salary *self.raise_amount
class Manager (Employee):
    def __init__(self, list_of_employee: list[Employee], department:str,first_name: str, last_name: str, mobile_number: int, salary: float):
        super().__init__(first_name, last_name, mobile_number, salary)
        self.list_of_employee = list_of_employee
        self.department =department
    def add_employee(self, new_employee:Employee):
        self.list_of_employee.append(new_employee)
    def remove_employee(self, employee:Employee):
        self.list_of_employee.remove(employee)
    def print_employee(self):
        for e in self.list_of_employee:
            print(e)
class Developer (Manager):#this is a multi-level inheritance
    def __init__(self, programming_language: str, list_of_employee: list[Employee], department: str, first_name: str,
                 last_name: str, mobile_number: int, salary: float):
        super().__init__(list_of_employee, department, first_name, last_name, mobile_number, salary)
        self.programming_language=programming_language
class Admin (Employee):#hierarchical inheritance
    def __init__(self, type_of_admin: str, first_name: str, last_name: str, mobile_number: int, salary: float):
        super().__init__(first_name, last_name, mobile_number, salary)
        self.type_of_admin =type_of_admin
class Programmer(Manager,Developer):#multiple with hybrid inheritance
    def __init__(self,skill_set:str):
        Manager.__init__()
        Developer.__init__()
        self.skill_set=skill_set
if __name__ == "__main__":
    employee =Employee("Daniel","ivron", 234246356, 204555.10)
    print(employee)
    Employee.print_company_name()
    print(employee.name)
    Employee.week_day_off()
    manager= Manager([employee], "finance","Mason","Smith",234235456,250000.10)
    print(manager.name)
    employee2=Employee("Jacub","Jackson",2342352,234523465)
    manager.add_employee(employee2)
    manager.print_employee()
