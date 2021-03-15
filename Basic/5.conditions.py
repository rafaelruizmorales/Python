#!/usr/bin/env python3

x = 2
print(x == 2) # True
print(x == 3) # False
print(x < 3)  # True

name = "John"
age  = 23

if name == "John" and age == 23:
  print("Your name is John 'AND' you are also 23 years old.")

if name == "John" or name == "Rick":
  print("Your name is either John 'OR' Rick.")

x = 2
if x < 2:
  print("x is less than 2")
elif x == 2:
  print("x equals 2!")
else:
  print("x is more than 2")

name = "John"
if name in ["John", "Rick"]:
  print("Your name is the List.")


x = [1,2,3]
y = [1,2,3]
print(x == y) # True
print(x is y) # False

print(not False)                #  True
print((not False) == (False))   #  False

print(0 == False)     # True => 0 is False!!!!
print(1 == True)      # True => 1 is True!!!!!

# There are no switch in python, so an alternative could be this... 
def switch(x):
  return {
      'a': 1,
      'b': 2
  }.get(x, 9)    # 9 is default if x not found

print(switch('c'))