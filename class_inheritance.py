class A(object):
	name="parent"
	
	def __fun1(self):
		print "This is parent's private"
	def funcall(self):
		__fun1()
		
	def fun2(self):
		print "class 1 without private"
		
class B(A):
	
	def fun(self):
		print "class 2"
		
		
		
a=B()
a.fun()
a.fun2()
#a.funcall() #gives error

class First(object):
  def __init__(self):

    print "first"
    super(First, self).__init__()

class Second(object):
  def __init__(self):
    
    print "second"
    super(Second, self).__init__()

class Third(First, Second):
  def __init__(self):
    
    print "that's it"
    super(Third, self).__init__()
    
class Fourth(object):
  def __init__(self):
    
    print "fourth"
    
Third()
print "--------------"

First()
