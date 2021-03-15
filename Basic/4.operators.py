#!/usr/bin/env python3

number = 1 + 2 * 3 / 4.0 # 1 + [(2 * 3) / 4.0] => 1 + (6 / 4) => 1 + 1.5 => 2.5
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2 # 7 * 7 => 49
print(squared)

cubed = 2 ** 3   # 2 * 2 * 2 => 8
print(cubed)

lol5 = "LOL " * 5
print(lol5)

evenNumbers = [2, 4, 6, 8]
oddNumbers  = [1, 3, 5, 7]
allNumbers  = oddNumbers + evenNumbers
print(allNumbers)


print(["L", "O", "L"] * 3)

myString = "0123456789_abcdefghi_0123456789"

#len(string)
print(len(myString))           # 31

# string.index("char")
print(myString.index('2'))     # 2

# string.count('char')
print(myString.count('2'))     # 2

# string[3:7] / [start:stop]
print(myString[0:10])           # 0123456789
print(myString[0:-11])          # 0123456789_abcdefghi

# string[3:7:2] / [start:stop:step]
print(myString[0:10:2])         # 02468
print(myString[11:0:-2])        # a97531

print(myString[::-1])           # 9876543210_ihgfedcba_9876543210

# string.upper()
print(myString.upper())         # 0123456789_ABCDEFGHI_0123456789

# string.lower()
print(myString.lower())         # 0123456789_abcdefghi_0123456789

# string.startswith(string)
print(myString.startswith("0123"))    # True

# string.endswith(string)
print(myString.endswith("0123"))      # False

# list = string.split('char') => PHP EXPLODE => String to List 
myList = myString.split("_")
print(myList)                   # ['0123456789', 'abcdefghi', '0123456789']