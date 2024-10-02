# calling stack demo

def a():
    print('a')
    b()

def b():
    print('b')
    c()

def c():
    first_name = 'Rhonda'
    print('c')

print(f'{a() = }')

# higher-order functions

def do_something(something):
    something()

def say_hello():
    print('Hello!')

do_something(say_hello)

def traverse(elements: list[float], operation):
    for elem in elements:
        operation(elem)

def print_square(value):
    print(f'{value * value}')

def is_prime(n):
    for div in range(2, n):
        if (n % div) == 0:
            print('False') 
    print('True')

print('Squares:')
traverse([1,2,3,4,5], print_square)

print('Primes:')
traverse([1,2,3,4,5], is_prime)

# map

def inches_to_cm(inches):
    return inches / 0.393701

measurements = [14.3, 74.0, 900.0, 8.4, 12.0]
cm_measurements = map(inches_to_cm, measurements)
print(f'{list(cm_measurements) = }')

# def scale(mark):
#     return mark + 30

midterm_marks = [39.0, 45.0, 55.5, 60.0, 17.0, 24.5]
# scaled_mt_marks = list(map(scale, midterm_marks))
scaled_mt_marks = list(map(lambda m: m + 30, midterm_marks))
print(f'{scaled_mt_marks = }')

# reduce

from functools import reduce 

def min2(a, b):
    if a < b:
        return a
    else:
        return b 
    
    # return a if a < b else b

project_scores = [30.0, 22.5, 27.0, 17.5, 22.0]
minimum = reduce(min2, project_scores)
print(f'{minimum = }')

# coding exercise 1

shopping_cart = [
    {'item_price': 19.99, 'quantity': 3},
    {'item_price': 2.99, 'quantity': 20},
    {'item_price': 9.99, 'quantity': 9},
    {'item_price': 29.99, 'quantity': 7},
    {'item_price': 199.99, 'quantity': 1},
]

def get_item_cost(item):
    return item['item_price'] * item['quantity']

item_costs = map(get_item_cost, shopping_cart)
# print(f'{list(item_costs) = }')

def add2(a, b):
    return a + b

subtotal = reduce(add2, item_costs)
print(f'${subtotal:.2f}')

# filter

def is_prime(n):
    for div in range(2, n):
        if (n % div) == 0:
            return False 
    return True 

primes = filter(is_prime, range(1, 100))
print(f'{list(primes) = }')
