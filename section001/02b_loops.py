x = 0
while x < 10:
    print(f'{x} is a single digit number.')
    x = x + 1

# use the defaults
for x in range(10):
    print(f'{x} is still a single digit number.')

# specify the values
for x in range(0, 10, 1):
    print(f'{x} is still a single digit number.')

for x in range(10, 0, -1):
    print(f'{x} was here.')

for c in 'abcdefghijklmnopqrdtuvwxyz':
    print(c)

# coding exercise 1
import math
# from math import factorial  

x = 1
estimate = 0.0
for n in range(100):
    exponent = x ** n
    fact = math.factorial(n)
    term = exponent / fact 
    estimate += term 

print(f'{estimate = }')

# hacker's corner

for x in (n**2 for n in [1,2,3,4,5]):
    print(f'{x = }')

print(list( (n**2 for n in [1,2,3,4,5]) ))