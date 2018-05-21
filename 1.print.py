#!/usr/bin/env python3

print("Hello World")

a = 1
if(a == 1):
  print("a is 1")

''' 
    %s - String (or any object with a string representation, like numbers)
    %d - Integers
    %f - Floating point numbers
    %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
    %x/%X - Integers in hex representation (lowercase/uppercase)
'''

myString = "hello"
if myString == "hello":
    print("String: %s" % myString)

myFloat = 10.0
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)

my2DecimalsFloat = 10.324343233245632
if isinstance(my2DecimalsFloat, float) and my2DecimalsFloat == 10.324343233245632:
    print("Float: %.2f" % my2DecimalsFloat)

myInt = 20
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)


name = "John"
age = 32
print("%s is %d years old." % (name, age))


mylist = [1,2,3]
print("A list: %s" % mylist)