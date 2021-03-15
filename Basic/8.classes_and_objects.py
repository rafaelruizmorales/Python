#!/usr/bin/env python3

class MyClass:
  variable = "blah"

  def myPublicMethod(self):
    print("I am public.")

  def __myPrivateMethod(self):
    print("I am private.")

myObject = MyClass()

print(myObject.variable)

myObject.myPublicMethod()
# myObject.__myPrivateMethod()    # This will fail since __myPrivateMethod is a private method
# but!!!....
'''
if we print the contents of myObject we will see the following:

print(dir(myObject))

[
  '_MyClass__myPrivateMethod', 
  
  '__class__', 
  '__delattr__', 
  '__dict__', 
  '__dir__', 
  '__doc__', 
  '__eq__', 
  '__format__', 
  '__ge__', 
  '__getattribute__', 
  '__gt__', 
  '__hash__', 
  '__init__', 
  '__init_subclass__', 
  '__le__', '__lt__', 
  '__module__', 
  '__ne__', 
  '__new__', 
  '__reduce__', 
  '__reduce_ex__', 
  '__repr__', 
  '__setattr__', 
  '__sizeof__', 
  '__str__', 
  '__subclasshook__', 
  '__weakref__', 
  'myPublicMethod', 
  'variable']
'''
# So we can actually access to the private method after all...
myObject._MyClass__myPrivateMethod()
