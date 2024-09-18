# coding challenge 02b.1
import math

x = 3.0 * math.pi / 2.0
estimate = 0.0
adding = True
for n in range(1, 100, 2):
    term = x ** n  / math.factorial(n)
    if adding:
        estimate += term 
    else:
        estimate -= term
    adding = not adding 

print(f'{estimate = }')

# coding challenge 02b.2
x = 7.0
low = 0.0
high = x
estimate = 0.0
epsilon = 0.00001

while abs(estimate**2 - x) > epsilon:
    estimate = (low + high) / 2.0

    if estimate ** 2 < x:
        low = estimate
    else:
        high = estimate 

print(f'{estimate = }')