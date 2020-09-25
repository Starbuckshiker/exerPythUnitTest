class Employee:
    
    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
       
    @property   
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
    def apply_raises(self)
        self.pay = int(self.pay * serlf.raise_amt)


emp_1 = Employee('Corer', 'Schafer', 50000)
emp_2 = Employee( 'Test', 'User', 60000)

#This allows you to adjust the instance of emp_1 instead of the class "Employee"
emp_1.raise_amount = 1.05
        
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)