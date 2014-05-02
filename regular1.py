import re
match=re.search("iipg","piiiiiiiiiig")
# if pattern is there it prints else error if we use group()
#match
if  match:print "cool"



def Find(pat,text):
    match=re.search(pat,text)

    #re.search() return a corresponding MatchObject instance. Return None
    # ***re.findall()  return a list of groups; this will be a list of tuples if the pattern has more than one group

'''tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
  print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
  for tuple in tuples:
    print tuple[0]  ## username
    print tuple[1]  ## host'''

    if match:print match.group()
    else: print "not found"

Find("...g","piiiig")
#match any three charters except newline before g

Find("p....g","piiiig")

Find("...p","piiiig")

#r'c\.' c.lled   ,\w diff . any char, \w word char ,\d\d\d  \s space
# \s+ lot space, \w+ lot word :.+ all from : \S no white space

#25 min
#35min
