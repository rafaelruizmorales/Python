#!/usr/bin/env python3

def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by zero!")
  else:
    print("result is", result)
  finally:
    print("executing finally clause")


divide(2, 1)
# result is 2.0
# executing finally clause

divide(2, 0)
# division by zero!
# executing finally clause

divide("2", "1")
# Traceback (most recent call last):
#   File "13.exceptions.py", line 22, in <module>
#     divide("2", "1")
#   File "13.exceptions.py", line 5, in divide
#     result = x / y
# TypeError: unsupported operand type(s) for /: 'str' and 'str'


# User-defined Exceptions #

class Error(Exception):
  """Base class for exceptions in this module."""
  pass

class InputError(Error):
  """Exception raised for errors in the input.

  Attributes:
      expression -- input expression in which the error occurred
      message -- explanation of the error
  """

  def __init__(self, expression, message):
    self.expression = expression
    self.message = message

class TransitionError(Error):
  """Raised when an operation attempts a state transition that's not
  allowed.

  Attributes:
      previous -- state at beginning of transition
      next -- attempted new state
      message -- explanation of why the specific transition is not allowed
  """

  def __init__(self, previous, next, message):
    self.previous = previous
    self.next = next
    self.message = message