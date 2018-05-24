#!/usr/bin/env python3

# Option 1
phonebook_1 = {}

phonebook_1["John"] = 111111111
phonebook_1["Jack"] = 222222222
phonebook_1["Jill"] = 333333333

print(phonebook_1)

# Option 2
phonebook_2 = {
    "John" : 111111111,
    "Jack" : 222222222,
    "Jill" : 333333333
}
print(phonebook_2)

# Iteration
for name, number in phonebook_2.items():
  print("Phone number of %s is %d" % (name, number))

# Add a value
phonebook_2["YunLong"] = 555555555
print(phonebook_2)

# Edit a value
phonebook_2["Jack"] = 666666666
print(phonebook_2)

# Remove a value
Jack = phonebook_2.pop("Jack")
print(Jack)
print(phonebook_2)