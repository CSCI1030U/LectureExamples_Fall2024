kid_age = 11
if kid_age < 10:
    print('Sorry but you cannot play the switch.')

if kid_age < 10:
    print('No switch today!')
else:
    print('Go ahead and play!')

kid_age = 11
if kid_age < 4:
    print('Maybe play with blocks.')
elif kid_age < 10:
    print('Use it in docked mode.')
elif kid_age < 16:
    print('Use it in handheld mode.')
else:
    print('You can even use my gaming PC.')

# programming exercise 02a.1

a = int(input('Enter a: '))
b = int(input('Enter b: '))

if (a % 2) == 0:
    # a is an even num 
    if (b % 2) == 0:
        # b is an even num
        print('Both numbers are even.')

if (a % 2) == 0 and (b % 2) == 0:
    print('Both numbers are even.')
