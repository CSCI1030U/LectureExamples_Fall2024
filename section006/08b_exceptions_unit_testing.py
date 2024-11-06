class FilenameTooLongException(Exception):
    pass 

def read_file_contents(filename):
    if len(filename) > 10:
        raise FilenameTooLongException('The filename must be <= 10 characters.')
    
    return 'abcde'

contents = read_file_contents('short.txt')
print(f'{contents = }')

try:
    # values= [1,2,3]
    # print(f'{values[4] = }')
    contents2 = read_file_contents('a_longer_filename.txt')
    print(f'{contents2 = }')
except FilenameTooLongException as error:
    print(f'{error = }')
except Exception as error:
    print('No idea what to do?')

print('All done')

# coding exercise 1

def print_reciprocals():
    for n in range(5, -1, -1):
        try:
            print(f'{1/n = }')
        except ZeroDivisionError as error:
            print('1/n caused a division by zero error')

print_reciprocals()

# coding exercise 2

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

import unittest 

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(0.123, 'Clarissa')
        self.assertEqual(clarissa.gpa, 0.123)
        self.assertEqual(clarissa.name, 'Clarissa')
        self.assertEqual(clarissa.marks, [])

    def test_set_mark(self):
        clarissa = Student(0.0, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 70.0)
        self.assertEqual(clarissa.marks, [70.0])
        clarissa.set_mark('MATH1010U', 52.5)
        self.assertEqual(clarissa.marks, [70.0,52.5])
    
    def test_get_average(self):
        clarissa = Student(0.0, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 70.0)
        clarissa.set_mark('MATH1010U', 50.0)
        self.assertAlmostEqual(clarissa.get_average(), 60.0, 0.001)


unittest.main()