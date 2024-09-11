student_age = 17
some_ratio = 3.1415926
alpha = 'abcdef'

# account_num = input('What is your account number? ')
account_num = '543'
print('Account num: ' + account_num)
print('Student age: ' + str(student_age))

message = f'Student age: {student_age}'
print(message)

print(f'Student age: {student_age}')
print(f'{student_age = }')

print(f'Pi rounded is {some_ratio:.2f}.')

print(f'{type(student_age)}')

is_hungry = True 
need_to_go_out = False
print(is_hungry and need_to_go_out)
print(f'{is_hungry or need_to_go_out=}')

y = 2
x = 1 + 8 / y

a = 5
b = 7
c = 9
print(f'{a=} {b=} {c=}')
avg = (a + b - c) / 3
print(f'{avg = }')

# coding exercise

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

sum = num1 + num2 
print(f'{sum % 5 = }')
