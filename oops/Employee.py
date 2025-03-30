class Employee:
    company_name = "Google"#class variable
    @classmethod#class method
    def calculate_salary(cls):
        print("your salary is 100$")
    def __init__(self,first_name,last_name,age,phone_number):
        self._first_name=first_name#protected data member
        self.last_name= last_name
        self.__age=age
        self.phone_number=phone_number
        print("this is a default constructor")
    def get_full_name(self):
        print(f"the first name is {self._first_name} and the last name is {self.last_name}")
    def get_age(self):
        print(f"the age is {self.__age}")
    def __private_method(self):
        print("this is a private method")
    def _protected_method(self):
        print("this is a protected method")
employee=Employee("Daniel","Ivron",14,12313424353)
employee.get_full_name()
employee.get_age()
Employee.company_name="Yahoo"
print(employee.company_name)
print(Employee.company_name)
employee.calculate_salary()
Employee.calculate_salary()
#print(employee._first_name)   can't access protected data member outside the class