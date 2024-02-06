#!/usr/bin/python3

def listBenfits():
    return [
        'More organized code',
        'More readable code',
        'Easier code reuse',
        'Allowing programmers to share and connect code together'
    ]

def buildSentance(benfit):
    return benfit + ' is a benfit of functions!'

def nameTheBenfitsOfFunction():
    listOfBenfits = listBenfits()

    for benfit in listOfBenfits:
        print(buildSentance(benfit))

nameTheBenfitsOfFunction()
