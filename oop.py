# python object oriented programming 

class Employee:
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + "comany.com"

    
        
emp_1 = Employee("Mateni", 'Yim' , '50000')
emp_2 = Employee('Test', 'User','6000')

##print(emp_1)
#print(emp_2)


print(emp_1.email)
print(emp_2.email)
