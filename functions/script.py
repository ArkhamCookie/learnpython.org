#!/usr/bin/python3

def myFunction():
    print('Hello from my function!')

myFunction()

def myFunctionWithArgs(username, greeting):
    print('Hello, %s , From My Function!, I wish you %s' % (username, greeting))

myFunctionWithArgs('ArkhamCookie', 'a happy holiday')

def sum2Numbers(a, b):
    return (a + b)

print(sum2Numbers(1, 5))
