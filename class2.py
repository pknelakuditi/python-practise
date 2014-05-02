 # class DerivedClass(BaseClass)
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
    def _work(self):
    	print "this is clss1 protected"

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
        
    def accessnew(self):
    	self.__new()
    	
    def __new(self):
        print "private"

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours=hours
        return hours*12.00
   # def newtest(self,hours):
    def new1(self):
        
        return super(PartTimeEmployee,self).__new()
	
    	
    	

    def full_time_wage(self,hours):
        self.hours=hours
        return super(PartTimeEmployee,self).calculate_wage(hours)

milton=PartTimeEmployee("Milton")
print milton.full_time_wage(10)
#milton.new1() gives error as it is as=ccessing private function of class emplyee
milton._work()
milton.accessnew()
pavan=Employee("pavan")
pavan._work()


"""

class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

"""
