n = 6
while n > 0:
    print(f'Smash! {n}')
    n = n - 1
    # n -= 1  (identical behaviour)

for x in range(0, 10, 1):
    print(x)

# default start: 0, default increment: 1
for x in range(10):
    print(x)

for y in range(10, 4, -1):
    print(f'{y = }')

n = 8
x = 1
for i in range(n):
    x = x * 2
print(f'{x = }')

max = 3000
x = 1
while x <= max:
    x = x * 2
print(f'{x//2 = }')

# exercise 02b.1
import math
# from math import factorial

x = 1
estimate = 0.0
for n in range(0, 1000, 1):
    exponent = x ** n 
    factorial = math.factorial(n)
    term = exponent / factorial
    estimate = estimate + term 

print(f'{estimate = }')

# hacker's corner
for x in (n ** 2 for n in range(10)):
    print(f'{x = }')
