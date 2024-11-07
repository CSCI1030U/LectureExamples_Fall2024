names = ['Carla', 'Susanne', 'Ahmed', 'Wil']

try:
    print(f'{names[4] = }')
except IndexError as error:
    print('No such name at that index!')
except Exception as error:
    print('Something else happened!')

print('After the error')

def print_names(names, indexes):
    for index in indexes:
        print(names[index])

# print_names(['Carla', 'Susanne', 'Ahmed', 'Wil'], [0, 2, 4])

class InsufficientFundsError(Exception):
    pass

def pay_bill(account_balance, bill_amount):
    if bill_amount > account_balance:
        raise InsufficientFundsError('Account balance too low to pay this bill.')

    return account_balance - bill_amount

try:
    new_balance = pay_bill(100.0, 160.0)
    print(f'{new_balance = }')
except InsufficientFundsError as error:
    print(f'Error while paying bill: {error}')
    # quit() # if you still want the application to stop - e.g. catastrophic error

print('After paying the bill')

# coding exercise 1

class InvalidReciprocalError(Exception):
    pass

# custom error - no handling
# def print_reciprocals(values):
#     for n in values:
#         if n == 0:
#             raise InvalidReciprocalError('Cannot calculate 1/0')
#         print(f'{1/n = }')

# handling the error
def print_reciprocals(values):
    for n in values:
        try:
            print(f'{1/n = }')
        except ZeroDivisionError as error:
            print('Cannot calculate 1/0.')

print_reciprocals([0,1,2,3,4,5])

def is_prime(n):
    for div in range(2,n):
        if (n % div) == 0:
            return False 
    return True

import unittest 

class IsPrime_Test(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(17))

# coding exercise 2

class NoMarksError(Exception):
    pass

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        if len(self.marks) == 0:
            raise NoMarksError('You cannot calculate an average of zero elements')
        
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
        clarissa = Student(0.0, 'Clarissa')
        # self.assertRaises(clarissa.get_average(), NoMarksError)
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertAlmostEqual(clarissa.get_average(), 70.0, 0.0000001)
        clarissa.set_mark('MATH1010U', 50.0)
        self.assertAlmostEqual(clarissa.get_average(), 60.0, 0.0000001)


unittest.main()

'''
Test cases for sort():

[4,1,5,2,3] -> [1,2,3,4,5]
[3,-1,2,-4,5] -> [-4,-1,2,3,5]
[7] -> [7]
[] -> []
'''