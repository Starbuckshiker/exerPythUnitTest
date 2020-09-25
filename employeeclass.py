class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
      #by naming this "Employee" instead of self it will count each instance  
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corer', 'Schafer', 50000)
emp_2 = Employee( 'Test', 'User', 60000)

#This allows you to adjust the instance of emp_1 instead of the class "Employee"
emp_1.raise_amount = 1.05
        
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)