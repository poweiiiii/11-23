class Employee:
    def __init__(self , emp_name, emp_id,emp_salary ,emp_department  ):
        self.name = emp_name
        self.id = emp_id
        self.salary = emp_salary
        self.department = emp_department
    def Employee_1(self):
        self.name = 'ADAMS'
        self.id = 'E7876'
        self.salary = 50000
        self.department = 'ACCOUNTING'
    def Employee_2(self):
        self.name = 'JONES'
        self.id = 'E7499'
        self.salary = 45000
        self.department = 'RESEARCH'
    def Employee_3(self):
        self.name = 'MARTIN'
        self.id = 'E7900'
        self.salary = 50000
        self.department = 'SALES'
    def Employee_4(self):
        self.name = 'SMITH'
        self.id = 'E7698'
        self.salary = 55000
        self.department = 'OPERATIONS'

    def new_assign_department(self):
        self.assign_department = self.department
        print(self.assign_department)

emp1 = Employee()
emp1.new_assign_department()