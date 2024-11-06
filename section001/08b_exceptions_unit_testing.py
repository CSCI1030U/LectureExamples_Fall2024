names = ['Barb', 'Kumar', 'Aleishia']

try:
    print(f'{names[3] = }')
except IndexError as error:
    print('Index [3] doesn\'t exist')

print('All done printing the 4th name')

class InsufficientFundsException(Exception):
    pass 

def buy_product(price, account_balance):
    if price > account_balance:
        raise InsufficientFundsException(f'You cannot afford ${price}.')
    account_balance -= price 
    print(f'{account_balance = }')

account_balance = 100.0
try:
    buy_product(150.0, account_balance)
except InsufficientFundsException as error:
    print('That costs too much, sorry!')

# coding exercise 1

class NoZeroAllowed(Exception):
    pass

def print_reciprocals(values):
    for n in values:
        # if n == 0:
        #     raise NoZeroAllowed('You cannot 1/0')
        try:
            print(f'{1/n = }')
        except ZeroDivisionError as error:
            print('Cannot calculate 1/0')

print_reciprocals([5,4,3,2,1,0])

shopping_cart = [
    {'product-id': 17723, 'quantity': 10},
    {'product-id': 53682, 'quantity': 1},
    {'product-id': 32704, 'quantity': 1},
    {'product-id': 8110, 'quantity': 2},
]

def search(values, to_find):
    for val in values:
        if val == to_find:
            return True 
    return False

import unittest 

class Search_Test(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([1,2,3,4,5], 3), True)
        self.assertTrue(search([1,2,3,4,5], 5))
        self.assertTrue(search([1,2,3,4,5], 1))
        self.assertFalse(search([1,2,3,4,5], 6))
        self.assertFalse(search([], 5))

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(0.123, 'Clarissa')
        self.assertEqual(clarissa.gpa, 0.123)
        self.assertEqual(clarissa.name, 'Clarissa')

    def test_set_mark(self):
        clarissa = Student(0.123, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertEqual(clarissa.marks, [70.0])
        clarissa.set_mark('MATH1010U', 50.0)
        self.assertEqual(clarissa.marks, [70.0, 50.0])

    def test_get_average(self):
        clarissa = Student(0.123, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 70.0)
        clarissa.set_mark('MATH1010U', 50.0)
        self.assertAlmostEqual(clarissa.get_average(), 60.0, 0.0000001)

unittest.main()

