#pythonpractice

items = [1,3,3,7]

for i in items:
    if i %2 == 0:
        print('Found Even Number: ', i)
else:
    print('No Even Number Found')


names = ['John', 'Jane', 'Doe']

for name in names:
    if name == 'Jane':
        print('Found Jane')
        break
else:
    print('Jane not found')