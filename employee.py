#import requests

class Employee:
    """A sample Employee Class"""

    raise_amt = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
       
    @property   
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    #def monthly_schedule(self, month):
        #response = requests.get(f'http://company.com/{self.last}/{month}')
        #if response.ok:
            #return response.text
        #else:
            #return 'Bad Response!'
            
emp_1 = Employee('Corer', 'Schafer', 50000)
emp_2 = Employee( 'Test', 'User', 60000)

#This allows you to adjust the instance of emp_1 instead of the class "Employee"
emp_1.raise_amount = 1.05
        
print(Employee.raise_amt)


