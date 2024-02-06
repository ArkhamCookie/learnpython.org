#!/usr/bin/python3

phonebook = {
    'John' : 938477566,
    'Jack' : 938377264,
}
phonebook['Jill'] = 947662781

print(phonebook)

for name, number in phonebook.items():
    print('Phone number of %s is %d' % (name, number))

del phonebook['John'] # or phonebook.pop('John')

print(phonebook)
