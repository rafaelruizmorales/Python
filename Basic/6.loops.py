#!/usr/bin/env python3

# The "for" loop
pizza = ["slice_1", "slice_2", "slice_3", "slice_4"]
for pizzaSlice in pizza:
  print(pizzaSlice)

# range

for x in range(5):
  print(x)        # 0,1,2,3,4

for x in range(3, 6):
  print(x)        # 3,4,5

for x in range(3, 8, 2):
  print(x)        # 3,5,7

# "while" loops
count = 0
while count < 5:
  print(count)
  count += 1  # This is the same as count = count + 1

# "break" and "continue" statements
count = 0
while True:
  print(count)
  count += 1
  if count >= 5:
    break

# Prints out only odd numbers => 1,3,5,7,9
for x in range(10):
  if x % 2 == 0:
    continue
  print(x)

# "else" clause for loops ^_^
count=0
while count < 5:
  print(count)
  count +=1
else:
  print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
  if i % 5 == 0:
    break
  print(i)
else:
  print("this is not printed because for loop is terminated because of break but not due to fail in condition")