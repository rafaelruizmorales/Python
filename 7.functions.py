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