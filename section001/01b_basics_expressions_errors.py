first_name = 'Randy'
last_name = "Fortier"
age = 49
important_ratio = 3.1415926

# name = input('What is your name? ')
name = 'Alexia'

print('Hello', name, '.')

greeting = f'Hello {name}.'
print(greeting)

print(f'You are {age:9d} years old.')
print(f'You are {age:09d} years old.')
print(f'Pi rounded is {important_ratio:.2f}.')

item_cost = 19.99
quantity = 5
subtotal = item_cost * quantity
print(f'${subtotal:.2f}')

# syntax error
# x = 

# runtime error
x = 10
y = 0
# z = x / y

a,b,c = 1,2,3
print(f'{a = }')
z = (a + b - c) / 3
print(f'{z = }')
