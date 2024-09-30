def a(message):
    print(f'a() message: {message}')
    b(message)

def b(message):
    print(f'b() message: {message}')
    c(message)

def c(message):
    print(f'c() message: {message}')

a('hello')

# higher order functions

def do_it_twice(something_to_do):
    '''
    this function does something twice idk
    '''
    something_to_do()
    something_to_do()

def say_yo():
    print('yo')

do_it_twice(say_yo)

def traverse_list(my_list, do_something):
    for element in my_list:
        do_something(element)

traverse_list([1,2,3,4], print)

def print_square(n):
    print(f'{n * n}')

traverse_list([1,2,3,4], print_square)

# map 

def feet_to_metres(feet):
    return feet * 0.3048

elevation_data = [0.0, 6.5, -5.0, 1.0, 350.0, 1100.0]

elevation_data_metric = []
for measurement in elevation_data:
    metres = feet_to_metres(measurement)
    elevation_data_metric.append(metres)

elevation_data_metric_map = map(feet_to_metres, elevation_data)
print(f'{list(elevation_data_metric_map) = }')

# reduce 

def min2(a, b):
    if a < b:
        return a 
    else:
        return b

from functools import reduce

marks = [55.0, 71.0, 62.0, 35.0, 19.5, 78.0, 87.0]
minimum = reduce(min2, marks)
print(f'{minimum = }')

product = reduce(lambda a,b: a * b, marks)
print(f'{product = }')

# filter
