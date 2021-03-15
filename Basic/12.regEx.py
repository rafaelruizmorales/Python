#!/usr/bin/env python3

# TO SEE: https://docs.python.org/3/howto/regex.html

import re

'''
IDENTIFIERS

\d
Matches any decimal digit; this is equivalent to the class [0-9]

\D
Matches any non-digit character; this is equivalent to the class [^0-9]

\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v]

\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v]

\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]

\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]


These sequences can be included inside a character class. For example:
[\s,.] is a character class that will match any whitespace character, or ',' or '.'

'.' is often used where you want to match “any character”

'''

# Exercise: make a regular expression that will match an email
import re
def test_email(your_pattern):
  pattern = re.compile(your_pattern)
  emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
  for email in emails:
      if not re.match(pattern, email):
          print("You failed to match %s" % (email))
      elif not your_pattern:
          print("Forgot to enter a pattern!")
      else:
          print("Pass")
          
# Your pattern here!
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)