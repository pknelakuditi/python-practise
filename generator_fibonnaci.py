def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

count =0
for i in fib():
    print i
    count+=1
    if count==15:
        break

def sum_iterable(a):
    return reduce(lambda x,y: x+y, a, 0)




def testgen():
    count=0
    while 1:
        yield count
        count+=1

c =0
for i in testgen():
    print i
    c+=1
    if c==15:
        break
