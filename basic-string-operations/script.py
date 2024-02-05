#!/usr/bin/python3

myString = 'Hello World!'

print(len(myString))

print(myString.index('o'))

print(myString.count('1'))

print(myString[3:7])

print(myString[3:7:2])

print(myString[::-1])

print(myString.upper())
print(myString.lower())

print(myString.startswith('Hello'))
print(myString.endswith('asdf'))

listOfWords = myString.split(" ")

print(listOfWords)
