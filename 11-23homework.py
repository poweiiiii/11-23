class Employee:
    def __init__(self ,name, id,salary ,department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department
        
    def assign_department(self , new_department):
        self.department = new_department

    def print_detail(self):
        print('{} {} {} {} '.format(self.name , self.id , self.salary , self.department))

    def overtime_bonus(self ,salary , worktime):
        overtime = 0
        if worktime > 50 :
            overtime = worktime - 50 
        self.salary = self.salary + (overtime * (self.salary / 50))

emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING" )
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH" )
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS" )

emp2.overtime_bonus(45000 ,63)
emp4.overtime_bonus(55000 , 59)       

emp2.assign_department('SALES')


emp1.print_detail()
emp2.print_detail()
emp3.print_detail()
emp4.print_detail()

