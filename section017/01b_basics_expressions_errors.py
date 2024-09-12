first_name = 'Randy'
# lastName = 'Fortier' # camel case
last_name = 'Fortier' # snake case

age = 49 # int (integer)
ratio = 3.1415926 # float (floating point, i.e. decimal/real almost)

print(64, 'Python')
print('Randy\nFortier') # newline: \n

print(first_name + last_name)
print(first_name, last_name)

greeting = 'Hello, ' + first_name + '. You are ' + str(age) + ' years old.'
greeting = f'Hello, {first_name}. You are {age} years old.'
print(greeting)

price = 200.712483684
print(f'The circle you want costs ${price:.2f}.')

item_cost = 19.99
quantity = 7
print(f'{item_cost = }')
print('item_cost = ' + str(item_cost))
subtotal = item_cost * quantity

first_name = input('What is your name? ')
print(f'Hello, {first_name}!')

# str(a) - convert 'a' into a string
# int(a) - convert 'a' into a integer
# float(a) - convert 'a' into a float

x = 17
x = x + 1
x += 1
# x++  # not in Python, sorry!
x -= 1

# syntax error
# x = 

# runtime error
y = 0
# z = x / y

# programming exercise

num1 = int(input('Enter the first number:  '))
num2 = int(input('Enter the second number: '))

sum = num1 + num2 
print(f'{sum % 5 = }')
