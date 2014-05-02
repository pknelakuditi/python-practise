my_dict={'pavan':"kumar","Age":23}

my_dict["uni"]='universtiy of florida'

print my_dict
del my_dict["uni"]
print my_dict

my_dict.pop("Age")


print my_dict.items()

#searching for keys in dictionary

print 'pavan' in my_dict
print my_dict.get("kumar")

print "----------------*************************__________________"
#understand iter functions


print my_dict

print "----------------"

#print my_dict.items()

print my_dict.keys()

y=my_dict.has_key('pavan')
print y

y=my_dict.has_key('weight')
print y

di=my_dict.copy()
print di

n=['pavan',"na"]
#use of fromkeys??
print my_dict.fromkeys(n)
print my_dict


print my_dict.values()

print zip(my_dict.values(),my_dict.keys())

my_dict.clear()
print my_dict

dit={'pavan':"kumar","Age":23}

for x in dit:
    print x,dit[x]

for x,v in dit.items():
    print x,v
#using string format from dictionary
print "%(pavan)s is " %dit

"""
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."


"""

for i in range(10):
	
	print i
	
