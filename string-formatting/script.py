#!/usr/bin/python3

name = 'John'
age = 23

print('%s is %d years old' % (name, age))

myList = [1,2,3]

print('A list: %s' % myList)

# Exercise
data = ('John', 'Doe', 53.44)
formatString = "Hello %s %s. Your current balance is $%.2f."

print(formatString % data)
