'''this is about dictionaries'''
#anonymous functions
SQUARES = [x**2 for x in range(1, 11)]
print filter(lambda x: x > 30 and x < 70, SQUARES)

#List Comprehension Syntax
EVEN_SQUARES = [x**2 for x in range(1, 11) if x%2 == 0]
print EVEN_SQUARES


GARBLED = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
MSG = GARBLED[:1:-2]
print MSG

 # class DerivedClass(BaseClass)
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    """this ptp"""
    def calculate_wage(self, hours):
        self.hours = hours
        return hours*12.00
    def full_time_wage(self, hours):
        self.hours = hours
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)

#dealing with the lists

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

al = range(51)
print al

MY_LIST = range(1, 11)

#Reversing a List

backwards = MY_LIST[::-1]
print backwards

#dictionary Usage

DICT1 = {'pavan':"kumar", "Age":23}

DICT1["uni"] = 'universtiy of florida'

print DICT1
del DICT1["uni"]
print DICT1

print DICT1.items()#return list of tuples 

print 'pavan' in DICT1 #True
#understand iter functions
#Y= DICT1.iteritems()
#print Y

#print DICT1.items()

print DICT1.keys()

Y = DICT1.has_key('pavan') #TRUE
print Y

Y = DICT1.has_key('weight')
print Y

DI = DICT1.copy()
print DI

N = ['pavan', "na"]
#use of fromkeys
print DICT1.fromkeys(N)
print DICT1

print DICT1.get('pavan')


#using default values
#default=20
#print DICT1.pop('Age'[,default])

print DICT1.values()

print zip(DICT1.values(), DICT1.keys())

DICT1.clear()
print DICT1

dit = {'pavan':"kumar", "Age":23}

for x in dit:
    print x, dit[x]
       

