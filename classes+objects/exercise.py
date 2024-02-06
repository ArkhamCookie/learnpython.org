#!/usr/bin/python3

class Vehicle:
    name = ''
    kind = 'car'
    color = ''
    value = 100.00

    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        descriptionString = '%s is a %s %s worth $%.2f' % (self.name, self.color, self.kind, self.value)
        return descriptionString

car1 = Vehicle('Fer', 'convertible', 'red', 60000.00)
car2 = Vehicle('Jump', 'van', 'blue', 1000.00)

print(car1.description())
print(car2.description())
