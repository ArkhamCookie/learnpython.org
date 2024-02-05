#!/usr/bin/python3

x = 2

print(x == 2)
print(x == 3)
print (x < 3)

# Boolean Operators
name = 'John'
age = 23

if name == 'John' and age == 23:
    print('Your name is John and you are also 23.')

if name == 'John' or name == 'Rick':
    print('Your name is either "John" or "Rick".')

# "in" Operator
if name in ['John', 'Rick']:
    print('Your name is either "John" or "Rick".')

# True/False
statment = False
statment2 = True

# If Statements
if statment:
    print('Statment is true.')
elif statment2:
    print('Statment 2 is true.')
else:
    print('Neither statment is true.')

if x == 2:
    print('x equals two.')
else:
    print('x does not equal two.')

## "is" Operator
x = [1,2,3]
y = [1,2,3]

print(x == y)
print(x is y)

# "not" Operator
print(not False)
print((not False) == (False))
