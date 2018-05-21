#!/usr/bin/env python3

# NUMBERS
myInt = 1
print(myInt)

myFloat = 7.5
print(myFloat)

myCastedFloat = float(myInt)
print(myCastedFloat)

a, b = 3, 4
print(a, b)

# STRINGS
myString = "Don't worry about apostrophes"
print(myString)

hello = "Hello"
world = "World"
helloworld = hello + " " + world
print(helloworld)

one = 1
two = 2
three = "3"

#print(one + two + hello)  # This will not work!
print(str(one) + str(two) + three) # int to str => str(int)