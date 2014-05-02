#dealing with the lists

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

al=range(51)
print al

my_list = range(1, 11)

backwards=my_list[::-1]
print backwards

print range(10).__getitem__(slice(0, 5, 2))
print range(10)[slice(0, 5, 2)]

