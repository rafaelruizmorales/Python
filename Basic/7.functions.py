#!/usr/bin/env python3

def my_function():
  print("Hello From My Function!")

my_function()

def my_function_with_args(username, greeting):
  print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_function_with_args("Rafa", "were here")
my_function_with_args(username="Rafa", greeting="were here")
# my_function_with_args(u="Rafa", g="were here")    # this fails!

def sum3(n1, n2, n3):
  return sum2(int(sum2(n1, n2)), int(n3))

def sum2(n1, n2):
  return int(n1) + int(n2)

print(sum3(1.5, "2", 3))

def foo(first, second, third, *therest):
  print("First: %s" % first)
  print("Second: %s" % second)
  print("Third: %s" % third)
  print("And all the rest... %s" % list(therest))

#foo(1,2)       This will fail
foo(1,2,3)
foo(1,2,3,4)
foo(1,2,3,4,5)

def calculate(n1, n2, **action):
  if action.get("operator") == "+":
    return n1 + n2 
  elif action.get("operator") == "*":
    return n1 * n2

print(calculate(7, 10, operator = "+"))
print(calculate(7, 10, operator = "*"))