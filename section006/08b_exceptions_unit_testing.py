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