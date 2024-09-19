# infinite loop
# x = 0
# while x < 10:
#     print(f'{x} is small.')
#     x = x - 1

# print(f'{x = }')

range(1, 5, 1) # => [1,2,3,4]

for x in [1,2,3,4,5,6,7,8,9]:
    print(f'{x} is a single digit number.')

for x in range(1, 10, 1):
    print(f'{x} is still a single digit num.')

for x in range(10):
    # zero is included since the start number has default of 0
    print(f'{x} is still a single digit number.')

# coding exercise 1

import math 

estimate = 0.0
x = 1
for n in range(100):
    # calculations go here
    exponent = x ** n 
    fact = math.factorial(n)
    estimate += exponent / fact 

print(f'{estimate = }')

# hacker's corner

for square in (x**2 for x in range(10)):
    print(f'{square = }')