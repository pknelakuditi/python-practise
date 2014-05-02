import cx_Oracle

db = cx_Oracle.connect('pkn', 'Nelakuditi1', 'oracle.cise.ufl.edu/orcl')
if db:print "connected"
c = db.cursor()

#c.execute('select * from city')
#for result in c:
 #   print result
 

c.execute('select table_name from user_tables')

for result in c:
 print result



"""
for dropping all the tables
c.execute('select table_name from user_tables')
lst=[]
for result in c:
 lst.append(result[0])  
 
print lst

for result in lst:
    s="DROP TABLE %s"%result 
    print s
    if(c.execute(s)):
     print "dropped %s"%result"""
    
  
#

db.close()
