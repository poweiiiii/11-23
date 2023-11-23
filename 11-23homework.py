class Employee:
    def __init__(self ,name, id,salary ,department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department
    def Employee_1(self):
        self.name = 'ADAMS'
        self.id = 'E7876'
        self.salary = 50000
        self.department = 'ACCOUNTING'
        print('{} {} {} {}'.format(self.name , self.id , self.salary , self.department))
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
emp = Employee()
emp.Employee_1()