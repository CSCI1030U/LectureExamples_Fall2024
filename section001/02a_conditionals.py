
kid_age = 7
if kid_age < 10:
    print('No you cannot use my switch!')

kid_age = 11
if kid_age < 10:
    print('You can use it, but it must stay in the dock.')
else:
    print('No problem, have fun!')

# too much effort, not worth it version
kid_age = 11
if kid_age < 10:
    print('You can use it, but it must stay in the dock.')
if kid_age >= 10:
    print('No problem, have fun!')

# programming exercise

a = int(input('Enter a: '))
b = int(input('Enter b: '))

if (a % 2) == 0:
    # a is an even number
    if (b % 2) == 0:
        # b is an even number
        print('Both numbers are even.')

if (a % 2) == 0 and (b % 2) == 0:
    print('Both numbers are even.')

# hacker's corner
name1 = 'Joseph'
name2 = 'Alice'
shorter_name = name1 if len(name1) < len(name2) else name2 
print(shorter_name)
