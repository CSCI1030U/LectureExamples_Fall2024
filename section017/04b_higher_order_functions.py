# calling stack
def a(message):
    print(f'from a(): {message}')
    b(message)

def b(message):
    print(f'from b(): {message}')
    c(message)

def c(message):
    print(f'from c(): {message}')

a('hello')

# higher-order functions
def traverse(elements, do_something):
    for elem in elements:
        do_something(elem)

import math
def print_sqrt(n):
    print(f"{math.sqrt(n)}")

# traverse([1,2,3], print_sqrt)

# map

def f_to_c(f):
    return (f - 32) * 5 / 9

f_temps = [40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
# for f_temp in f_temps:
#     print(f_to_c(f_temp))
c_temps = map(f_to_c, f_temps)
print(f'{list(c_temps) = }')

# reduce 
from functools import reduce

def mult2(a, b):
    return a * b

marks = [39.0, 55.0, 62.5, 42.0, 74.5, 90.0, 100.0, 11.5, 52.0]
product = reduce(mult2, marks)
print(f'{product = }')

def min2(a, b):
    if a < b:
        return a 
    else:
        return b 
min_mark= reduce(min2, marks)
print(f'{min_mark = }')

# hacker's corner

product = reduce(lambda a,b: a * b, marks)
print(f'{product = }')

min_mark = reduce(lambda x,y: x if x < y else y, marks)
print(f'{min_mark = }')

# filter

def failing_grade(mark):
    if mark < 50.0:
        return True 
    else:
        return False 

failing_marks = filter(failing_grade, marks)
print(f'{list(failing_marks) = }')

# coding exercise 1

invoice_items = [
    {'item_price': 19.99, 'quantity': 5},
    {'item_price': 14.99, 'quantity': 1},
    {'item_price': 11.99, 'quantity': 3},
    {'item_price': 9.99, 'quantity': 4},
]

def add_items(item1, item2):
    return item1 + item2

def get_cost(item):
    return item['item_price'] * item['quantity']

subtotal = reduce(add_items, map(get_cost, invoice_items))
print(f'{subtotal = }')

