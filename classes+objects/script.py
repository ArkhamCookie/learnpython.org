#!/usr/bin/python3

class MyClass:
    variable = 'blah'

    def function(self):
        print('This is a message inside the class.')

myObjectX = MyClass()

print(myObjectX.variable)

myObjectY = MyClass()
myObjectY.variable = 'yackity'

print(myObjectY.variable)

# Accessing Object Functions

myObjectX.function()

# init()

class NumberHolder:
    def __init__(self, number):
        self.number = number

myNumber = NumberHolder(5)

print(myNumber.number)
