#!/usr/bin/env python3

'''
Generators are simple functions which return an iterable set of items, 
one at a time, in a special way.

When an iteration over a set of item starts using the for statement, the generator is run. 
Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. 
The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

'''

# EXAMPLE 1

import random

def lottery():
  # returns 6 numbers between 1 and 5
  for i in range(6):
      yield random.randint(1, 5)

  # returns a 7th number between 1 and 50
  yield random.randint(1,50)

for random_number in lottery():
  print("And the next number is... %d!" %(random_number))

# EXAMPLE 2

def fibonacci():
  a, b = 1, 1
  while 1:
    yield a
    a, b = b, a + b

import types

if type(fibonacci()) == types.GeneratorType:
  print("Good, The fibonacci function is a generator.")

  counter = 0
  for n in fibonacci():
    print(n)
    counter += 1
    if counter == 10:
      break